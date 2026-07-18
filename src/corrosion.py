"""
corrosion.py
---------------------------------
Copper corrosion model
"""


def corrosion_rate(
    temperature,
    sulfide,
    ph
):
    """
    Simplified corrosion model.
    Returns corrosion rate in mm/year.
    """

    base_rate = 0.0005

    temperature_factor = 1 + 0.015 * (temperature - 15)

    sulfide_factor = 1 + 100 * sulfide

    ph_factor = 1 - 0.03 * (ph - 7)

    rate = (
        base_rate
        * temperature_factor
        * sulfide_factor
        * ph_factor
    )

    return rate


def remaining_thickness(
    initial_thickness,
    corrosion_rates
):
    """
    Calculates remaining copper thickness.

    corrosion_rates must be in mm/year.
    """

    thickness = []

    current = initial_thickness

    for rate in corrosion_rates:

        current = current - rate

        thickness.append(current)

    return thickness