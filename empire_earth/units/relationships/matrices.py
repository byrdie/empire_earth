from typing import List, Callable
import numpy as np
import pandas
from ..unit import Unit


def _matrix(func_name: str, units: List[Unit]) -> pandas.DataFrame:

    result = []

    for unit_attacker in units:
        result_row = [unit_attacker.name]

        for unit_defender in units:
            value_attacker = getattr(unit_attacker, func_name)(unit_defender)
            value_defender = getattr(unit_defender, func_name)(unit_attacker)
            if value_defender == 0:
                if value_attacker == 0:
                    value = np.nan
                else:
                    value = np.inf
            else:
                value = value_attacker / value_defender
            # value = unit_attacker.attack_final(unit_defender)
            # value = unit_attacker.damage_dealt_per_hit(unit_defender)
            result_row.append(value)

        result.append(result_row)

    result = pandas.DataFrame(result, columns=['Attacker'] + [unit.name for unit in units])

    return result


def matrix_tactical(units: List[Unit]) -> pandas.DataFrame:
    return _matrix('fractional_damage_dealt_per_second', units)


def matrix_strategic(units: List[Unit]) -> pandas.DataFrame:
    return _matrix('fractional_damage_dealt_per_second_per_resource', units)