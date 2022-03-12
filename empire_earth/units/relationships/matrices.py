from typing import List, Callable
import numpy as np
import pandas
from ..unit import Unit


def stylize(df: pandas.DataFrame):
    gmap = np.log10(df.to_numpy())
    return df.style.set_sticky('rows').background_gradient(
        axis=None,
        cmap='bwr_r',
        vmin=-2,
        vmax=2,
        gmap=gmap,
    )


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
    result = result.set_index('Attacker')

    return result


def matrix_tactical(units: List[Unit]) -> pandas.DataFrame:
    return stylize(_matrix('fractional_damage_dealt_per_second', units))


def matrix_strategic(units: List[Unit]) -> pandas.DataFrame:
    return stylize(_matrix('fractional_damage_dealt_per_second_per_resource', units))