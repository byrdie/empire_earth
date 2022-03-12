from typing import Dict
import pathlib
import pickle
import struct
import pandas

path_base = pathlib.Path(__file__).parent


def dbobjects_struct() -> pandas.DataFrame:
    return pandas.read_csv(
        path_base / 'dbobject_struct.csv',
        names=['field name', 'cX', 'num_bytes', 'dtype'],
        index_col=0,
    )


def dbobjects() -> pandas.DataFrame:
    cache = path_base / 'dbobjects.pickle'

    if not cache.exists():
        result = _calc_dbobjects()
        with open(cache, 'wb') as handle:
            pickle.dump(result, handle, protocol=pickle.HIGHEST_PROTOCOL)

    else:
        with open(cache, 'rb') as handle:
            result = pickle.load(handle)

    return result


def _calc_dbobjects() -> pandas.DataFrame:
    """
    .. jupyter-execute::
        
        import empire_earth.databases
        
        dbobjects = empire_earth.databases.dbobjects()
        dbobjects.style.set_sticky('columns')
    """
    dbobjects_structure = dbobjects_struct()

    columns = [index for index, row in dbobjects_structure.iterrows()]

    result = []

    with open(path_base / 'dbobjects.dat', 'rb') as file:

        file.read(4)

        escape = False
        while True:

            result_row = []

            for index, row in dbobjects_structure.iterrows():
                num_bytes = row['num_bytes']
                datum = file.read(num_bytes)
                if not datum:
                    escape = True
                    break
                dtype = row['dtype']
                if dtype == 1:
                    if num_bytes == 4:
                        value = struct.unpack('i', datum)[0]
                    else:
                        value = datum.decode(errors='ignore')
                elif dtype == 2:
                    value = datum.decode(errors='ignore')
                    value = value.replace('\x00', '')
                elif dtype == 3:
                    value = struct.unpack('f', datum)[0]
                result_row.append(value)

            if escape:
                break

            result.append(result_row)

    result = pandas.DataFrame(result, columns=columns)

    return result.set_index('DB Name')

def dbfamily() -> pandas.DataFrame:

    columns = ['family name', 'c1', 'family index']

    result = []

    num_fields = 71

    with open(path_base / 'dbfamily.dat', 'rb') as file:

        file.read(4)

        escape = False
        while True:
            result_row = []

            for i in range(num_fields):
                if i == 0:
                    num_bytes = 100
                else:
                    num_bytes = 4
                datum = file.read(num_bytes)
                if not datum:
                    escape = True
                    break
                if i == 0:
                    value = datum.decode('utf-8').replace('\x00', '')
                elif i < 3:
                    value = struct.unpack('i', datum)[0]
                else:
                    value = struct.unpack('i', datum)[0] / 100
                result_row.append(value)

            if escape:
                break

            result.append(result_row)

    columns = columns + list(range(num_fields - len(columns)))

    return pandas.DataFrame(result, columns=columns).set_index('family index')


def epoch_span() -> pandas.DataFrame:
    return pandas.read_csv(path_base / 'epoch_span.csv', index_col=0)


def dbweapontohit() -> pandas.DataFrame:
    columns = ['Weapon Hit Name', 'c1', 'Weapon Hit ID']

    result = []

    num_fields = 9

    with open(path_base / 'dbweapontohit.dat', 'rb') as file:

        file.read(4)

        escape = False
        while True:
            result_row = []

            for i in range(num_fields):
                if i == 0:
                    num_bytes = 100
                else:
                    num_bytes = 4
                datum = file.read(num_bytes)
                if not datum:
                    escape = True
                    break
                if i == 0:
                    value = datum.decode('utf-8').replace('\x00', '')
                    # columns.append(value)
                elif i < 3:
                    value = struct.unpack('i', datum)[0]
                else:
                    value = struct.unpack('i', datum)[0] / 100
                result_row.append(value)

            if escape:
                break

            result.append(result_row)

            columns = columns + list(range(num_fields - len(columns)))

    return pandas.DataFrame(result, columns=columns).set_index('Weapon Hit ID')

def dbtechtree(num_epoch: int = 15) -> Dict[str, pandas.DataFrame]:



    result = dict()

    num_bytes_per_name = 28
    num_bytes_per_field = 4
    num_bytes_per_tech = 272
    num_bytes_all_fields = num_bytes_per_tech - num_bytes_per_name
    num_bytes_per_link = 272

    num_fields_per_tech = int(num_bytes_all_fields / num_bytes_per_field) + 1

    # print('num_fields_per_tech', num_fields_per_tech)

    with open(path_base / 'dbtechtree.dat', 'rb') as file:

        for index_epoch in range(num_epoch):

            # print('index_epoch', index_epoch)

            num_techs = struct.unpack('i', file.read(4))[0] + 1

            # print('num_techs', num_techs)

            result_epoch = []
            for index_tech in range(num_techs):

                # print('index_tech', index_tech)

                result_epoch_tech = []
                for index_field in range(num_fields_per_tech):

                    # print('index_field', index_field)

                    if index_field == 0:
                        num_bytes = num_bytes_per_name
                    else:
                        num_bytes = 4
                    datum = file.read(num_bytes)

                    if index_field == 0:
                        value = [datum.decode(errors='ignore').replace('\x00', '')]

                    elif 51 <= index_field <= 54:
                        value = struct.unpack('f', datum)

                    elif index_field in [39, 55]:
                        value = struct.unpack('????', datum)

                    else:
                        # print('datum', datum)
                        value = struct.unpack('i', datum)

                        if index_field == num_fields_per_tech - 1:
                            num_fields_extra = value[0]

                            for index_field_extra in range(num_fields_extra):
                                v = struct.unpack('i', file.read(num_bytes_per_field))[0]
                                if v < result_epoch_tech[~0]:
                                    result_epoch_tech[~0] = v

                    result_epoch_tech += value

                # print(result_epoch_tech[0])
                if result_epoch_tech[0]:
                    result_epoch.append(result_epoch_tech)

            result_epoch = pandas.DataFrame(result_epoch)
            mapping_columns = {
                20: 'Technology ID',
                21: 'Starting Epoch',
                22: 'Ending Epoch',
                25: 'Wood Cost',
                26: 'Stone Cost',
                28: 'Gold Cost',
                30: 'Iron Cost',
                31: 'Food Cost',
                32: 'Build Time Decrease',
                33: 'Upgrade Tech ID',
                37: 'Object ID',
                38: 'Button ID',
                46 + 3: 'Button Index',
                57 + 3 + 3: 'Epoch',
                59 + 3 + 3: 'Base Technology ID',
                60 + 3 + 3: 'Building ID',
            }
            result_epoch = result_epoch.rename(columns=mapping_columns)
            result_epoch = result_epoch.set_index('Technology ID')
            result[index_epoch] = result_epoch

    return result




def language() -> pandas.DataFrame:
    return pandas.read_csv(path_base / 'Language.txt', names=['value'], index_col=0)
