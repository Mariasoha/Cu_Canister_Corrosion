"""
corrosion.py
---------------------------------
Copper corrosion model
"""

import numpy as np


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