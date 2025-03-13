import pandas as pd
import numpy as np

# Reproducibility ke liye seed set karein
np.random.seed(42)

num_samples = 1000

# Random data generate karein for features:
air_pollution_index = np.random.uniform(0, 100, num_samples)   # 0 se 100 tak
co2_emissions = np.random.uniform(0, 500, num_samples)           # 0 se 500 tak
industrial_waste = np.random.uniform(0, 200, num_samples)        # 0 se 200 tak

# EnergyRecovered target variable: 
# Yeh ek dummy relationship hai (aap apni logic laga sakte hain)
energy_recovered = (air_pollution_index * 0.5) + (co2_emissions * 0.2) - (industrial_waste * 0.1) + np.random.normal(0, 10, num_samples)

# DataFrame banayein
df = pd.DataFrame({
    "AirPollutionIndex": air_pollution_index,
    "CO2Emissions": co2_emissions,
    "IndustrialWaste": industrial_waste,
    "EnergyRecovered": energy_recovered
})

# CSV file mein data likhein (ye file aapke current directory mein ban jayegi)
df.to_csv("data.csv", index=False)

print("CSV file 'data.csv' successfully created!")
