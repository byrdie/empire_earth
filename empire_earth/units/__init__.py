from typing import List, Dict
from empire_earth import databases
from .unit import Armor, Attack, Unit


def units_all() -> Dict[str, Unit]:

    dbobjects = databases.dbobjects()
    dblanguage = databases.language()
    dbfamily = databases.dbfamily()
    dbweapontohit = databases.dbweapontohit()
    databases.epoch_span()

    result = dict()

    for index, row in dbobjects.iterrows():

        id_language = row['Language ID']
        if id_language in dblanguage.index:
            name = dblanguage.loc[id_language].to_numpy()[0].replace('"', '').lstrip(' ')
            unit = Unit(
                name=name,
                id=row['Object ID'],
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
                dbfamily=dbfamily,
                dbweapontohit=dbweapontohit,
            )
            result[name] = unit

    return result


def units_military() -> Dict[str, Unit]:
    units = units_all()
    units = {name: units[name] for name in units if units[name].attack > 0}
    return units