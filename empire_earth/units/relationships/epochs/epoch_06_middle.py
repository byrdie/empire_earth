"""

===========================
Tactical Unit Relationships
===========================

.. jupyter-execute::

    import empire_earth.units.relationships.matrices

    epoch = 6
    units = empire_earth.units.attackers(epoch)
    empire_earth.units.relationships.matrices.matrix_tactical(units.values())

============================
Strategic Unit Relationships
============================

.. jupyter-execute::

    empire_earth.units.relationships.matrices.matrix_strategic(units.values())

"""