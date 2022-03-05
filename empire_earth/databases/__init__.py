import pathlib
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


def weapon_to_hit_map() -> pandas.DataFrame:
    return pandas.read_csv(path_base / 'weapontohit_export.csv', index_col=2)['Unnamed: 0']


def language() -> pandas.DataFrame:
    return pandas.read_csv(path_base / 'Language.txt', names=['value'], index_col=0)
