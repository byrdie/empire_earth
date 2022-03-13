"""
=====
Units
=====

.. jupyter-execute::

    import pandas
    import empire_earth.units.relationships.matrices

    epoch = 5
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