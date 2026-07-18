"""
main.py
---------------------------------
Copper Canister Corrosion Model

Module 6
Repository + Materials + Groundwater + Temperature + Corrosion
"""
from groundwater_evolution import sulfide_concentration
from repository import load_repository_conditions, get_parameter
from materials import load_material_database, get_material
from groundwater import load_groundwater_database
from groundwater import get_parameter as get_groundwater_parameter
from temperature import repository_temperature
from corrosion import corrosion_rate, remaining_thickness

import numpy as np
import matplotlib.pyplot as plt


def main():

    print("=" * 50)
    print("Copper Canister Corrosion Simulation")
    print("=" * 50)

    # =====================================
    # Load repository database
    # =====================================

    repository = load_repository_conditions(
        "data/repository_conditions.csv"
    )

    initial_temperature = float(
        get_parameter(repository, "InitialTemperature")
    )

    ambient_temperature = float(
        get_parameter(repository, "AmbientTemperature")
    )

    decay_constant = float(
        get_parameter(repository, "DecayConstant")
    )

    simulation_years = int(
        get_parameter(repository, "SimulationYears")
    )

    # =====================================
    # Load material database
    # =====================================

    materials = load_material_database(
        "data/material_properties.csv"
    )

    copper = get_material(
        materials,
        "Copper"
    )

    print("\nCopper Material Properties")
    print("-" * 30)
    print(f"Density               : {copper['Density']} kg/m³")
    print(f"Thermal Conductivity  : {copper['ThermalConductivity']} W/m·K")
    print(f"Specific Heat         : {copper['SpecificHeat']} J/kg·K")
    print(f"Young's Modulus       : {copper['YoungsModulus']} GPa")

    # =====================================
    # Load groundwater database
    # =====================================

    groundwater = load_groundwater_database(
        "data/groundwater.csv"
    )

    ph = get_groundwater_parameter(
        groundwater,
        "pH"
    )["Value"]

    chloride = get_groundwater_parameter(
        groundwater,
        "Chloride"
    )["Value"]

    sulfide = get_groundwater_parameter(
        groundwater,
        "Sulfide"
    )["Value"]

    oxygen = get_groundwater_parameter(
        groundwater,
        "DissolvedOxygen"
    )["Value"]

    eh = get_groundwater_parameter(
        groundwater,
        "Eh"
    )["Value"]

    print("\nGroundwater Chemistry")
    print("-" * 30)
    print(f"pH                 : {ph}")
    print(f"Chloride           : {chloride} mg/L")
    print(f"Sulfide            : {sulfide} mg/L")
    print(f"Dissolved Oxygen   : {oxygen} mg/L")
    print(f"Redox Potential    : {eh} mV")

    # =====================================
    # Temperature calculation
    # =====================================

    years = np.arange(0, simulation_years + 1)

    temperature = repository_temperature(
        years,
        initial_temperature,
        ambient_temperature,
        decay_constant
    )
    # =====================================
    # Sulfide evolution
    # =====================================

    sulfide_history = []

    increase_rate = 0.000004

    for year in years:

        current_sulfide = sulfide_concentration(
            year,
            sulfide,
            increase_rate
        )

        sulfide_history.append(current_sulfide)

    # =====================================
    # Corrosion calculation
    # =====================================

    corrosion_rates = []

    for i in range(len(years)):

        rate = corrosion_rate(
            temperature[i],
            sulfide_history[i],
            ph
        )

        corrosion_rates.append(rate)

    print("\nFirst 10 Sulfide Values")
    print("-" * 30)

    for i in range(10):
        print(
            f"Year {years[i]:4d} : "
            f"{sulfide_history[i]:.6f} mg/L"
        )
    # =====================================
    # Remaining copper thickness
    # =====================================

    initial_thickness = 50.0

    thickness = remaining_thickness(
        initial_thickness,
        corrosion_rates
    )

    print("\nCopper Corrosion")
    print("-" * 30)
    print(f"Repository Temperature : {temperature[0]:.2f} °C")
    print(f"Estimated Corrosion Rate : {corrosion_rates[0]:.6f} mm/year")

    print("\nFirst 10 Remaining Thickness Values")
    print("-" * 35)

    for i in range(10):
        print(
            f"Year {years[i]:4d} : "
            f"{thickness[i]:.3f} mm"
        )

    # =====================================
    # Print temperatures
    # =====================================

    print("\nFirst 10 Temperatures")

    for i in range(10):
        print(
            f"Year {years[i]:4d} : "
            f"{temperature[i]:6.2f} °C"
        )

    # =====================================
    # Plot temperature
    # =====================================

    print("\nCreating temperature graph...")

    plt.figure(figsize=(10, 6))

    plt.plot(
        years,
        temperature,
        linewidth=2,
        label="Repository Temperature"
    )

    plt.title("Repository Temperature vs Time")
    plt.xlabel("Time (Years)")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()

    plt.savefig(
        "figures/temperature_profile.png",
        dpi=300
    )

    plt.close()

    print("Temperature graph saved!")


if __name__ == "__main__":
    main()