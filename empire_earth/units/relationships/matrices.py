from typing import Dict
import pandas
from ..unit import Unit


def matrix_tactical(units: Dict[str, Unit]) -> pandas.DataFrame:

    result = []

    for unit_name_attacker in units:
        unit_attacker = units[unit_name_attacker]
        result_row = [unit_name_attacker]

        for unit_name_defender in units:
            unit_defender = units[unit_name_defender]
            value = unit_attacker.fractional_damage_dealt_per_second(unit_defender)
            result_row.append(value)

        result.append(result_row)

    result = pandas.DataFrame(result, columns=list(units.keys()))

    return result