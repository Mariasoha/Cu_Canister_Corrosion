"""
main.py
---------------------------------
Copper Canister Corrosion Model

Module 1
Repository Temperature
"""

import numpy as np
import matplotlib.pyplot as plt

from temperature import repository_temperature


def main():

    print("=" * 50)
    print("Copper Canister Corrosion Simulation")
    print("=" * 50)

    years = np.arange(0, 1001)

    initial_temperature = 90

    ambient_temperature = 15

    decay_constant = 0.003

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