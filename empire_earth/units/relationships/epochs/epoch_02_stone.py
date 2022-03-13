"""
=====
Units
=====

.. jupyter-execute::

    import pandas
    pandas.set_option('display.max_columns', 1000)
    pandas.set_option('display.max_rows', 1000)
    pandas.set_option('display.max_colwidth', 200)

    import empire_earth.units.relationships.matrices

    epoch = 2
    units = empire_earth.units.attackers(epoch)
    pandas.DataFrame(units.values())

===========================
Tactical Unit Relationships
===========================

.. jupyter-execute::

    empire_earth.units.relationships.matrices.matrix_tactical(units.values())

============================
Strategic Unit Relationships
============================

.. jupyter-execute::

    empire_earth.units.relationships.matrices.matrix_strategic(units.values())

"""