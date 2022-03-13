import dataclasses
import pandas



@dataclasses.dataclass
class Unit:
    name: str = ''
    id: int = 0
    type_id: int = 0
    family: int = 0
    building: str = ''
    button_id: int = 0
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
    epoch_start: int = 0
    epoch_stop: int = 0
    cost_food: int = 0
    cost_wood: int = 0
    cost_stone: int = 0
    cost_iron: int = 0
    cost_gold: int = 0
    dbfamily: pandas.DataFrame = dataclasses.field(default_factory=pandas.DataFrame, repr=False)
    dbweapontohit: pandas.DataFrame = dataclasses.field(default_factory=pandas.DataFrame, repr=False)

    @property
    def cost_total(self) -> int:
        return self.cost_food + self.cost_wood + self.cost_stone + self.cost_iron + self.cost_gold

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
        attack = self.attack_final(defender)
        if attack == 0:
            return 0.
        else:
            damage = attack - defender.armor_final(self)
            damage = max(1, damage)
            return damage

    def damage_dealt_per_second(self, defender: 'Unit'):
        return self.damage_dealt_per_hit(defender) / self.seconds_per_attack

    def fractional_damage_dealt_per_second(self, defender: 'Unit'):
        return self.damage_dealt_per_second(defender) / defender.hitpoints

    def fractional_damage_dealt_per_second_per_resource(self, defender: 'Unit'):
        return self.fractional_damage_dealt_per_second(defender) / self.cost_total

    def is_available(self, epoch: int):
        return self.epoch_start <= epoch <= self.epoch_stop

    @property
    def theater_id(self):
        type_id_map = {
            2: 'Land Building',
            3: 'Planes',
            4: 'Ships',
            5: 'Land',
            6: 'Citizen',
            7: 'Helicopters',
            10: 'Submarines',
            13: 'Hero',
            17: 'Helicopters',
            23: 'Hero',
        }
        ordering_map = [
            'Land',
            'Citizen',
            'Hero',
            'Land Building',
            'Ships',
            'Submarines',
            'Planes',
            'Helicopters',
        ]
        ordering_map = {item: ordering_map.index(item) for item in ordering_map}
        return ordering_map[type_id_map[self.type_id]]

    @property
    def building_id_sorted(self):
        ordering_map = [
            'Barracks',
            'Stable',
            'Archery Range',
            'Tank Factory',
            'Cyber Factory',
            'Cyber Laboratory',
            'Siege Factory',
            'Citizen',
            'Single Player Settlement',
            'Town Center',
            'Capitol',
            'Dock',
            'Naval Yard',
            'Carrier - Enterprise',
            'Airport',
        ]
        ordering_map = {item: ordering_map.index(item) for item in ordering_map}
        return ordering_map[self.building]
