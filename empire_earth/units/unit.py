import dataclasses
import pandas

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
    attack: float = 0
    attack_mode: int = 0
    seconds_per_attack: float = 0
    weapon_hit_id: int = 0
    armor_shock: float = 0
    armor_arrow: float = 0
    armor_pierce: float = 0
    armor_gun: float = 0
    armor_laser: float = 0
    armor_missile: float = 0
    dbfamily: pandas.DataFrame = dataclasses.field(default_factory=pandas.DataFrame, repr=False)
    dbweapontohit: pandas.DataFrame = dataclasses.field(default_factory=pandas.DataFrame, repr=False)
    epoch_start: int = 0
    epoch_stop: int = 0

    def attack_multiplier_family(self, defender: 'Unit'):
        return self.dbfamily.loc[defender.family, self.attack_mode]

    def attack_multiplier_weapontohit(self, defender: 'Unit'):
        return self.dbweapontohit.loc[defender.weapon_hit_id, self.weapon_hit_id]

    def attack_multiplier(self, defender: 'Unit'):
        return self.attack_multiplier_family(defender) * self.attack_multiplier_weapontohit(defender)

    def attack_final(self, defender: 'Unit'):
        return self.attack * self.attack_multiplier(defender)

    def armor_final(self, attacker: 'Unit'):
        weapon_hit_id = attacker.weapon_hit_id
        if weapon_hit_id == 0:
            return self.armor_shock
        elif weapon_hit_id == 1:
            return self.armor_arrow
        elif weapon_hit_id == 2:
            return self.armor_pierce
        elif weapon_hit_id == 3:
            return self.armor_gun
        elif weapon_hit_id == 4:
            return self.armor_laser
        elif weapon_hit_id == 5:
            return self.armor_missile
        else:
            raise ValueError

    def damage_dealt_per_hit(self, defender: 'Unit'):
        return self.attack_final(self) - defender.armor_final(self)

    def damage_dealt_per_second(self, defender: 'Unit'):
        return self.damage_dealt_per_hit(defender) / self.attack.seconds_per_hit

    def fractional_damage_dealt_per_second(self, defender: 'Unit'):
        return self.damage_dealt_per_second(defender) / defender.hitpoints

    def is_available(self, epoch: int):
        return self.epoch_start <= epoch <= self.epoch_stop