"""
FormuLab
========

A mathematical and scientific computation toolkit for Python.
"""

__version__ = "0.1.0"

from .math import (
    add,
    subtract,
    multiply,
    divide,
    power,
    square_root,
    factorial,
    percentage,
    quadratic_roots,
    circle_area,
    circle_circumference,
    rectangle_area,
    triangle_area,
)

from .physics import (
    velocity,
    acceleration,
    distance,
    force,
    momentum,
    kinetic_energy,
    potential_energy,
    work,
    power,
    density,
    pressure,
    frequency_from_period,
    period_from_frequency,
    wavelength,
    wave_speed,
    ohms_law,
    electrical_power,
    electrical_energy,
)

from .statistics import (
    mean,
    median,
    variance,
    standard_deviation,
)

from . import constants