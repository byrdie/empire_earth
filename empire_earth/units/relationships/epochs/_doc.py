def calc(epoch: int):
    return f"""
=====
Units
=====

.. jupyter-execute::

    import pandas
    pandas.set_option('display.max_columns', 1000)
    pandas.set_option('display.max_rows', 1000)
    pandas.set_option('display.max_colwidth', 200)

    import empire_earth.units.relationships.matrices

    epoch = {epoch}
    units = empire_earth.units.attackers(epoch).values()
    pandas.DataFrame(units)

===========================
Damage Dealt per Hit
===========================

.. jupyter-execute::

    empire_earth.units.relationships.matrices.matrix_damage_dealt_per_hit(units)

===========================
Damage Dealt per Second
===========================

.. jupyter-execute::

    empire_earth.units.relationships.matrices.matrix_damage_dealt_per_second(units)

===========================
Tactical Unit Relationships
===========================

.. jupyter-execute::

    empire_earth.units.relationships.matrices.matrix_tactical(units)

============================
Strategic Unit Relationships
============================

.. jupyter-execute::

    empire_earth.units.relationships.matrices.matrix_strategic(units)

"""