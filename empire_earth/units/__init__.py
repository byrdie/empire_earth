from typing import List, Dict, Optional
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

    ignored_units = [
        'SAS Commando',
        'Spitfire Fighter',
        'ME109  Fighter/Bomber',
        'Heinkel Bomber',
    ]

    for index, row in dbobjects.iterrows():

        id_language = row['Language ID']
        if id_language in dblanguage.index:
            name = dblanguage.loc[id_language].to_numpy()[0].replace('"', '').lstrip(' ')
            if name in ignored_units:
                continue

            if '(Fire)' in name:
                # print(' - skipping', name)
                continue

            if '(Crusader)' in name:
                # print(' - skipping', name)
                continue

            object_id = index
            if object_id == -1:
                continue

            tech_id = row['Technology ID']
            if tech_id not in dbtechtree.index:
                # print(' - skipping', name)
                continue

            row_techtree = dbtechtree.loc[tech_id]

            if row_techtree[58] and row_techtree[59] and row_techtree[60] and row_techtree[61]:
                # print(' - skipping', name)
                continue

            if row_techtree['Button Index'] == -1:
                # print(' - skipping', name)
                continue

            if row_techtree['Object ID'] == -1:
            #     print(' - skipping', name)
                continue

            mask_building = dbtechtree['Building ID'] == row_techtree['Building ID']
            mask_button = dbtechtree['Button Index'] == row_techtree['Button Index']
            mask_epoch = dbtechtree['Starting Epoch'] > row_techtree['Starting Epoch']
            rows_upgrades = dbtechtree[mask_building & mask_button & mask_epoch]

            if not rows_upgrades.empty:
                epoch_stop = min(rows_upgrades['Starting Epoch'].min() - 1, row_techtree['Ending Epoch'])
            else:
                epoch_stop = row_techtree['Ending Epoch']

            building_id = row_techtree['Building ID']
            if building_id > 0:
                building_row = dbobjects.loc[building_id]
                building_name = dblanguage.loc[building_row['Language ID']].to_numpy()[0].replace('"', '').lstrip(' ')
            else:
                building_name = ''

            unit = Unit(
                name=name,
                id=object_id,
                type_id=row['Unit Type ID'],
                family=row['Family'],
                building=building_name,
                button_id=row_techtree['Button Index'],
                hitpoints=row['Health'],
                speed=row['Speed'],
                range=row['Max Range'],
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


def attackers(epoch: Optional[int] = None) -> Dict[str, Unit]:

    def is_attacker(unit: Unit, epoch: Optional[int]):
        return unit.attack > 0 and unit.seconds_per_attack > 0 and unit.is_available(epoch) and unit.building != 'Town Center'

    units = all()
    units = [units[name] for name in units if is_attacker(units[name], epoch)]
    units.sort(key=lambda unit: unit.button_id)
    units.sort(key=lambda unit: unit.cost_total)
    units.sort(key=lambda unit: unit.theater_id)
    units.sort(key=lambda unit: unit.building_id_sorted)
    units = {unit.name: unit for unit in units}
    return units
