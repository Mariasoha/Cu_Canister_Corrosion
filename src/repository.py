"""
repository.py
------------------------------------
Loads repository conditions
from CSV database.
"""

import pandas as pd


def load_repository_conditions(filename):

    data = pd.read_csv(filename)

    return data


def get_parameter(data, parameter):

    row = data[data["Parameter"] == parameter]

    return row["Value"].values[0]