import pathlib
import pandas

path_base = pathlib.Path(__file__).parent


def dbobject():
    return pandas.read_csv(path_base / 'object_export.csv')


def family():
    return pandas.read_csv(path_base / 'family_export.csv')


def epoch_span():
    return pandas.read_csv(path_base / 'epoch_span.csv')


def attack_multiplier():
    return pandas.read_csv(path_base / 'attack_mult_export.csv')
