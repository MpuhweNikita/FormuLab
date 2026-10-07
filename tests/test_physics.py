import pytest

from formulab import (
    velocity,
    acceleration,
    force,
    momentum,
    kinetic_energy,
    potential_energy,
    wave_speed,
    ohms_law,
)


def test_velocity():
    assert velocity(100, 5) == 20


def test_acceleration():
    assert acceleration(10, 30, 5) == 4


def test_force():
    assert force(10, 9.81) == pytest.approx(98.1)


def test_momentum():
    assert momentum(10, 5) == 50


def test_kinetic_energy():
    assert kinetic_energy(10, 5) == 125


def test_potential_energy():
    assert potential_energy(10, 10) == pytest.approx(981)


def test_wave_speed():
    assert wave_speed(10, 5) == 50


def test_ohms_law():
    assert ohms_law(2, 10) == 20