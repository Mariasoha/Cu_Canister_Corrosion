"""
temperature.py

Repository cooling model
"""

import numpy as np


def repository_temperature(
    years,
    initial_temperature,
    rock_temperature,
    cooling_constant
):
    """
    Exponential cooling model

    T(t) = Trock + (T0 - Trock)e^(-kt)
    """

    temperature = (
        rock_temperature +
        (initial_temperature - rock_temperature)
        * np.exp(-cooling_constant * years)
    )

    return temperature