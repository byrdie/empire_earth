from typing import List, Dict
import pandas
from empire_earth import databases
from .unit import Unit


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

            if object_id == -1:
                continue

            if object_id not in dbtechtree.index:
                continue

            row_techtree = dbtechtree.loc[object_id]

            mask_building = dbtechtree['Building ID'] == row_techtree['Building ID']
            mask_button = dbtechtree['Button Index'] == row_techtree['Button Index']
            mask_epoch = dbtechtree['Starting Epoch'] > row_techtree['Starting Epoch']
            rows_upgrades = dbtechtree[mask_building & mask_button & mask_epoch]

            if not rows_upgrades.empty:
                epoch_stop = rows_upgrades['Starting Epoch'].min() - 1
            else:
                epoch_stop = row_techtree['Ending Epoch']

            unit = Unit(
                name=name,
                id=object_id,
                family=row['Family'],
                hitpoints=row['Health'],
                attack=row['Attack'],
                attack_mode=row['Attack Mode'],
                seconds_per_attack=row['Attack Speed'],
                weapon_hit_id=row['Weapon Hit ID'],
                armor_shock=row['Shock Armor'],
                armor_pierce=row['Pierce Armor'],
                armor_gun=row['Gun Armor'],
                armor_laser=row['Laser Armor'],
                armor_missile=row['Missile Armor'],
                epoch_start=row_techtree['Starting Epoch'],
                epoch_stop=epoch_stop,
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
    units = {name: units[name] for name in units if units[name].attack > 0}
    return units
