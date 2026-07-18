"""
groundwater.py
---------------------------------
Groundwater chemistry database
"""

import pandas as pd


def load_groundwater_database(filename):

    return pd.read_csv(filename)


def get_parameter(data, parameter):

    row = data[data["Parameter"] == parameter]

    return row.iloc[0]