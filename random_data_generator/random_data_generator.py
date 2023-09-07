import numpy as np
import matplotlib.pyplot as plt

# Function to generate random data from different distributions
def generate_data(distribution, params, size=1000):
    if distribution == "normal":
        mean, std = params
        data = np.random.normal(mean, std, size)
    elif distribution == "uniform":
        low, high = params
        data = np.random.uniform(low, high, size)
    elif distribution == "exponential":
        scale = params
        data = np.random.exponential(scale, size)
    else:
        raise ValueError("Invalid distribution choice")
    return data

# Function to analyze and plot data
def analyze_and_plot_data(data, distribution_name):
    mean = np.mean(data)
    median = np.median(data)
    std = np.std(data)
    
    # Plot histogram
    plt.hist(data, bins=30, alpha=0.5, label=distribution_name)
    
    # Print statistics
    print(f"{distribution_name.capitalize()} Distribution Statistics:")
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std:.2f}")
    print("\n")

# User-defined parameters
normal_params = (0, 1)
uniform_params = (0, 10)
exponential_params = 2
sample_size = 1000

# Generate data for different distributions
normal_data = generate_data("normal", normal_params, sample_size)
uniform_data = generate_data("uniform", uniform_params, sample_size)
exponential_data = generate_data("exponential", exponential_params, sample_size)

# Analyze and plot data for each distribution
analyze_and_plot_data(normal_data, "normal")
analyze_and_plot_data(uniform_data, "uniform")
analyze_and_plot_data(exponential_data, "exponential")

# Customize the plot
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Random Data from Various Distributions")
plt.legend()
plt.grid(True)

# Show the combined plot
plt.show()
