import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic oil and gas well data
np.random.seed(0)
depth = np.linspace(1000, 4000, 100)  # Depth values (in meters)
porosity = np.random.uniform(0.1, 0.25, 100)  # Porosity values
permeability = np.random.uniform(1, 100, 100)  # Permeability values (in millidarcies)

# Basic data analysis
mean_porosity = np.mean(porosity)
median_permeability = np.median(permeability)
std_deviation_porosity = np.std(porosity)

# Data visualization
plt.figure(figsize=(10, 5))

# Porosity histogram
plt.subplot(1, 2, 1)
plt.hist(porosity, bins=20, color='blue', alpha=0.7)
plt.xlabel('Porosity')
plt.ylabel('Frequency')
plt.title('Porosity Histogram')

# Permeability histogram
plt.subplot(1, 2, 2)
plt.hist(permeability, bins=20, color='green', alpha=0.7)
plt.xlabel('Permeability (mD)')
plt.ylabel('Frequency')
plt.title('Permeability Histogram')

plt.tight_layout()
plt.show()

# Print basic statistics
print(f"Mean Porosity: {mean_porosity:.2f}")
print(f"Median Permeability: {median_permeability:.2f}")
print(f"Standard Deviation of Porosity: {std_deviation_porosity:.2f}")
