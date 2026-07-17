"""
=========================================
Copper Canister Corrosion Project
constants.py

Loads all engineering input data.
=========================================
"""

import pandas as pd
from pathlib import Path

# -------------------------------
# Project Paths
# -------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_FOLDER = PROJECT_ROOT / "data"

# -------------------------------
# CSV Files
# -------------------------------

MATERIAL_FILE = DATA_FOLDER / "material_properties.csv"
REPOSITORY_FILE = DATA_FOLDER / "repository_conditions.csv"
GROUNDWATER_FILE = DATA_FOLDER / "groundwater.csv"

# -------------------------------
# Read CSV Files
# -------------------------------

materials = pd.read_csv(MATERIAL_FILE)

repository = pd.read_csv(REPOSITORY_FILE)

groundwater = pd.read_csv(GROUNDWATER_FILE)

print("\nMaterial Properties")
print(materials)

print("\nRepository Conditions")
print(repository)

print("\nGroundwater Chemistry")
print(groundwater)
