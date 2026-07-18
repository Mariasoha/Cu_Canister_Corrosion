"""
groundwater_evolution.py
---------------------------------
Groundwater chemistry evolution
"""


def sulfide_concentration(
    year,
    initial_sulfide,
    increase_rate
):
    """
    Calculates sulfide concentration over time.
    """

    sulfide = (
        initial_sulfide
        + increase_rate * year
    )

    return sulfide