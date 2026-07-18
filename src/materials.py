"""
materials.py
--------------------------------
Material database
"""

import pandas as pd


def load_material_database(filename):

    return pd.read_csv(filename)


def get_material(data, material):

    row = data[data["Material"] == material]

    return row.iloc[0]