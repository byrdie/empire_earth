from typing import List, Callable
import numpy as np
import pandas
from ..unit import Unit


def stylize(matrix: pandas.DataFrame):
    gmap = np.log10(matrix.to_numpy())
    return matrix.style.format(formatter='{:.2f}').set_sticky('rows').background_gradient(
        axis=None,
        cmap='bwr_r',
        vmin=-1,
        vmax=1,
        gmap=gmap,
    )


def _matrix(func_name: str, units: List[Unit]) -> pandas.DataFrame:

    result = []

    for unit_attacker in units:
        result_row = [unit_attacker.name]

        for unit_defender in units:
            value = getattr(unit_attacker, func_name)(unit_defender)
            result_row.append(value)

        result.append(result_row)

    result = pandas.DataFrame(result, columns=['Attacker'] + [unit.name for unit in units])
    result = result.set_index('Attacker')
    result.index.name = None

    return result


def matrix_damage_dealt_per_hit(units: List[Unit]) -> pandas.DataFrame:
    matrix = _matrix('damage_dealt_per_hit', units).astype('int')
    gmap = np.log10(matrix.to_numpy())
    return matrix.style.set_sticky('rows').background_gradient(
        axis=None,
        cmap='viridis',
        vmin=-0.1,
        gmap=gmap,
    )


def matrix_damage_dealt_per_second(units: List[Unit]) -> pandas.DataFrame:
    matrix = _matrix('damage_dealt_per_second', units)
    gmap = np.log10(matrix.to_numpy())
    return matrix.style.format(':.2f').set_sticky('rows').background_gradient(
        axis=None,
        cmap='viridis',
        vmin=-0.1,
        gmap=gmap,
    )


def matrix_tactical(units: List[Unit]) -> pandas.DataFrame:
    return stylize(_matrix('ratio_fractional_damage_dealt_per_second', units))


def matrix_strategic(units: List[Unit]) -> pandas.DataFrame:
    return stylize(_matrix('ratio_fractional_damage_dealt_per_second_per_resource', units))