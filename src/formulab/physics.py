"""
Physics formulas for FormuLab.

The functions in this module cover common mechanics,
electricity, waves, and general physics calculations.
"""


def velocity(distance: float, time: float) -> float:
    """Calculate velocity using v = d / t."""
    if time == 0:
        raise ZeroDivisionError("Time cannot be zero.")
    return distance / time


def acceleration(
    initial_velocity: float,
    final_velocity: float,
    time: float,
) -> float:
    """Calculate acceleration using a = (v - u) / t."""
    if time == 0:
        raise ZeroDivisionError("Time cannot be zero.")
    return (final_velocity - initial_velocity) / time


def distance(
    initial_velocity: float,
    time: float,
    acceleration_value: float = 0.0,
) -> float:
    """Calculate distance using s = ut + ½at²."""
    return (
        initial_velocity * time
        + 0.5 * acceleration_value * time**2
    )


def force(mass: float, acceleration_value: float) -> float:
    """Calculate force using F = ma."""
    return mass * acceleration_value


def momentum(mass: float, velocity_value: float) -> float:
    """Calculate momentum using p = mv."""
    return mass * velocity_value


def kinetic_energy(mass: float, velocity_value: float) -> float:
    """Calculate kinetic energy using KE = ½mv²."""
    return 0.5 * mass * velocity_value**2


def potential_energy(
    mass: float,
    height: float,
    gravity: float = 9.81,
) -> float:
    """Calculate gravitational potential energy using PE = mgh."""
    return mass * gravity * height


def work(force_value: float, distance_value: float) -> float:
    """Calculate mechanical work using W = Fd."""
    return force_value * distance_value


def power(work_value: float, time: float) -> float:
    """Calculate power using P = W / t."""
    if time == 0:
        raise ZeroDivisionError("Time cannot be zero.")
    return work_value / time


def density(mass: float, volume: float) -> float:
    """Calculate density using ρ = m / V."""
    if volume == 0:
        raise ZeroDivisionError("Volume cannot be zero.")
    return mass / volume


def pressure(force_value: float, area: float) -> float:
    """Calculate pressure using P = F / A."""
    if area == 0:
        raise ZeroDivisionError("Area cannot be zero.")
    return force_value / area


def frequency_from_period(period: float) -> float:
    """Calculate frequency using f = 1 / T."""
    if period == 0:
        raise ZeroDivisionError("Period cannot be zero.")
    return 1 / period


def period_from_frequency(frequency: float) -> float:
    """Calculate period using T = 1 / f."""
    if frequency == 0:
        raise ZeroDivisionError("Frequency cannot be zero.")
    return 1 / frequency


def wavelength(
    wave_speed_value: float,
    frequency: float,
) -> float:
    """Calculate wavelength using λ = v / f."""
    if frequency == 0:
        raise ZeroDivisionError("Frequency cannot be zero.")
    return wave_speed_value / frequency


def wave_speed(
    frequency: float,
    wavelength_value: float,
) -> float:
    """Calculate wave speed using v = fλ."""
    return frequency * wavelength_value


def ohms_law(current: float, resistance: float) -> float:
    """Calculate voltage using Ohm's law V = IR."""
    return current * resistance


def electrical_power(
    voltage: float,
    current: float,
) -> float:
    """Calculate electrical power using P = VI."""
    return voltage * current


def electrical_energy(
    power_value: float,
    time: float,
) -> float:
    """Calculate electrical energy using E = Pt."""
    return power_value * time