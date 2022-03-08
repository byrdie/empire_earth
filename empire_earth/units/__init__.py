from typing import List, Dict
import pandas
from empire_earth import databases
from .unit import Unit

from . import relationships


def all() -> Dict[str, Unit]:

    dbobjects = databases.dbobjects()
    dblanguage = databases.language()
    dbfamily = databases.dbfamily()
    dbweapontohit = databases.dbweapontohit()
    dbtechtree = databases.dbtechtree()
    dbtechtree = pandas.concat(dbtechtree.values())

    result = dict()

    for index, row in dbobjects.iterrows():

        id_language = row['Language ID']
        if id_language in dblanguage.index:
            name = dblanguage.loc[id_language].to_numpy()[0].replace('"', '').lstrip(' ')
            object_id = row['Object ID']
            tech_id = row['Technology ID']

            if '(Fire)' in name:
                print(' - skipping', name)
                continue

            if '(Crusader)' in name:
                print(' - skipping', name)
                continue

            if object_id == -1:
                continue

            if tech_id not in dbtechtree.index:
                print(' - skipping', name)
                continue

            row_techtree = dbtechtree.loc[tech_id]

            if row_techtree[58] and row_techtree[59] and row_techtree[60] and row_techtree[61]:
                print(' - skipping', name)
                continue

            # if row_techtree['Button Index'] == -1:
            #     print(' - skipping', name)
            #     continue
            #
            # if row_techtree['Object ID'] == -1:
            #     print(' - skipping', name)
            #     continue

            mask_building = dbtechtree['Building ID'] == row_techtree['Building ID']
            mask_button = dbtechtree['Button Index'] == row_techtree['Button Index']
            mask_epoch = dbtechtree['Starting Epoch'] > row_techtree['Starting Epoch']
            rows_upgrades = dbtechtree[mask_building & mask_button & mask_epoch]

            if not rows_upgrades.empty:
                epoch_stop = min(rows_upgrades['Starting Epoch'].min() - 1, row_techtree['Ending Epoch'])
            else:
                epoch_stop = row_techtree['Ending Epoch']

            unit = Unit(
                name=name,
                id=object_id,
                type_id=row['Unit Type ID'],
                family=row['Family'],
                building_id=row_techtree['Building ID'],
                hitpoints=row['Health'],
                attack=row['Attack'],
                attack_mode=row['Attack Mode'],
                seconds_per_attack=row['Attack Speed'],
                weapon_hit_id=row['Weapon Hit ID'],
                armor_shock=row['Shock Armor'],
                armor_arrow=row['Arrow Armor'],
                armor_pierce=row['Pierce Armor'],
                armor_gun=row['Gun Armor'],
                armor_laser=row['Laser Armor'],
                armor_missile=row['Missile Armor'],
                epoch_start=row_techtree['Starting Epoch'] + 1,
                epoch_stop=epoch_stop + 1,
                cost_food=row_techtree['Food Cost'],
                cost_wood=row_techtree['Wood Cost'],
                cost_stone=row_techtree['Stone Cost'],
                cost_iron=row_techtree['Iron Cost'],
                cost_gold=row_techtree['Gold Cost'],
                dbfamily=dbfamily,
                dbweapontohit=dbweapontohit,
            )
            result[name] = unit

    return result


def attackers() -> Dict[str, Unit]:
    units = all()
    units = {name: units[name] for name in units if units[name].attack > 0 and units[name].seconds_per_attack > 0}
    return units
