import numpy as np
import matplotlib.pyplot as plt

import constants
from temperature import repository_temperature

# ----------------------------------------
# Simulation time
# ----------------------------------------

years = np.arange(0, 10001)

# ----------------------------------------
# Repository temperatures
# ----------------------------------------

initial_temperature = 90
rock_temperature = 15
cooling_constant = 0.001

temperature = repository_temperature(
    years,
    initial_temperature,
    rock_temperature,
    cooling_constant
)

print("First 10 temperatures:")

for i in range(10):
    print(
        f"Year {years[i]} : "
        f"{temperature[i]:.2f} °C"
    )