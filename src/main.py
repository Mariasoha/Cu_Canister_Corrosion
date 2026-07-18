"""
main.py
---------------------------------
Copper Canister Corrosion Model

Module 2
Repository Temperature using CSV
"""

from repository import load_repository_conditions, get_parameter
from temperature import repository_temperature

import numpy as np
import matplotlib.pyplot as plt


def main():

    print("=" * 50)
    print("Copper Canister Corrosion Simulation")
    print("=" * 50)

    # Load repository data
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

    # Simulation years
    years = np.arange(0, simulation_years + 1)

    # Temperature calculation
    temperature = repository_temperature(
        years,
        initial_temperature,
        ambient_temperature,
        decay_constant
    )

    print()
    print("First 10 temperatures")

    for i in range(10):
        print(
            f"Year {years[i]:4d} : "
            f"{temperature[i]:6.2f} °C"
        )

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

    plt.savefig("figures/temperature_profile.png", dpi=300)
    plt.show()

    print("Temperature graph saved!")


if __name__ == "__main__":
    main()