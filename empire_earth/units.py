from typing import List, Dict
import dataclasses
from empire_earth import databases

dbobjects = databases.dbobjects()
dblanguage = databases.language()
dbfamily = databases.dbfamily()
dbweapontohit = databases.dbweapontohit()


@dataclasses.dataclass
class Attack:
    strength: float = 0
    seconds_per_hit: float = 0
    mode: int = 0
    weapon_hit_id: int = 0


@dataclasses.dataclass
class Armor:
    shock: float = 0
    arrow: float = 0
    pierce: float = 0
    gun: float = 0
    laser: float = 0
    missile: float = 0


@dataclasses.dataclass
class Unit:
    name: str = ''
    id: int = 0
    family: int = 0
    hitpoints: float = 0
    attack: Attack = dataclasses.field(default_factory=Attack)
    armor: Armor = dataclasses.field(default_factory=Armor)
    epoch_start: int = 0
    epoch_stop: int = 0

    def attack_multiplier_family(self, defender: 'Unit'):
        return dbfamily.loc[defender.family, self.attack.mode]

    def attack_multiplier_weapontohit(self, defender: 'Unit'):
        return dbweapontohit.loc[defender.attack.weapon_hit_id, self.attack.weapon_hit_id]

    def attack_multiplier(self, defender: 'Unit'):
        return self.attack_multiplier_family(defender) * self.attack_multiplier_weapontohit(defender)

    def attack_final(self, defender: 'Unit'):
        return self.attack.strength * self.attack_multiplier(defender)

    def armor_final(self, attacker: 'Unit'):
        weapon_hit_id = attacker.attack.weapon_hit_id
        if weapon_hit_id == 0:
            return self.armor.shock
        elif weapon_hit_id == 1:
            return self.armor.arrow
        elif weapon_hit_id == 2:
            return self.armor.pierce
        elif weapon_hit_id == 3:
            return self.armor.gun
        elif weapon_hit_id == 4:
            return self.armor.laser
        elif weapon_hit_id == 5:
            return self.armor.missile
        else:
            raise ValueError

    def damage_dealt_per_hit(self, defender: 'Unit'):
        return self.attack_final(self) - defender.armor_final(self)

    def damage_dealt_per_second(self, defender: 'Unit'):
        return self.damage_dealt_per_hit(defender) / self.attack.seconds_per_hit

    def fractional_damage_dealt_per_second(self, defender: 'Unit'):
        return self.damage_dealt_per_second(defender) / defender.hitpoints


def units_all() -> Dict[str, Unit]:

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
                attack=Attack(
                    strength=row['Attack'],
                    seconds_per_hit=row['Attack Speed'],
                    mode=row['Attack Mode'],
                    weapon_hit_id=row['Weapon Hit ID'],
                ),
                armor=Armor(
                    shock=row['Shock Armor'],
                    pierce=row['Pierce Armor'],
                    gun=row['Gun Armor'],
                    laser=row['Laser Armor'],
                    missile=row['Missile Armor'],
                ),
            )
            result[name] = unit

    return result
