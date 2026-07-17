"""
temperature.py
-------------------------------
Repository Temperature Module

Author : Maria
Project: Copper Canister Corrosion Model

This module calculates repository temperature
using an exponential cooling equation.
"""

import numpy as np


def repository_temperature(
        years,
        initial_temperature,
        ambient_temperature,
        decay_constant):
    """
    Calculate repository temperature.

    Parameters
    ----------
    years : numpy.ndarray
        Simulation time

    initial_temperature : float
        Initial canister temperature (°C)

    ambient_temperature : float
        Host rock temperature (°C)

    decay_constant : float
        Cooling constant (1/year)

    Returns
    -------
    numpy.ndarray
        Temperature profile
    """

    temperature = ambient_temperature + (
        initial_temperature - ambient_temperature
    ) * np.exp(-decay_constant * years)

    return temperature