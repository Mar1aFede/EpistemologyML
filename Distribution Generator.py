#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:46:34 2023

@author: molly
script for creating distributions
One is selected by the user though the interface, while the other distribution, actually a range of distribution, 
is gathered from the first one but filtered by limitations of human learners or, equivalently, "biased" by some limitations,
such as noise, missing values.
"""

import numpy as np
import matplotlib.pyplot as plt

# Function to generate a distribution based on distribution type
def generate_distribution(distribution_type, size, mean, std_dev):
    # Define distribution generators using a dictionary
    distribution_generators = {
        'Gaussian': lambda: np.random.normal(mean, std_dev, size),
        'Uniform': lambda: np.random.uniform(mean - std_dev, mean + std_dev, size),
        'Exponential': lambda: np.random.exponential(scale=std_dev, size=size),
        'Poisson': lambda: np.random.poisson(mean, size),
        'Log-Normal': lambda: np.random.lognormal(mean, std_dev, size),
    }

    # Check if the specified distribution type is valid
    if distribution_type not in distribution_generators:
        raise ValueError("Invalid distribution type")

    # Generate and return the distribution
    return distribution_generators[distribution_type]()

# Functions to apply different human limitations

# Apply cognitive bias to the distribution
def apply_cognitive_bias(distribution):
    return distribution * 0.9

# Apply memory limitations to the distribution
def apply_memory_limitations(distribution):
    return distribution[:len(distribution) // 2]

# Apply sensory limitations (add noise) to the distribution
def apply_sensory_limitations(distribution):
    return np.random.normal(distribution, scale=0.1)

# Apply biased sampling (filter out negative values) to the distribution
def apply_biased_sampling(distribution):
    return distribution[distribution > 0]

# Apply computational limitations to the distribution
def apply_computational_limitations(distribution):
    return distribution[:len(distribution) // 2]

# Main function
def main():
    print("Welcome to the Distribution Generator and Filter:")
    distribution_type = input("Enter distribution type (Gaussian/Uniform/Exponential/Poisson/Log-Normal): ")
    size = int(input("Enter size of the distribution: "))
    mean = float(input("Enter mean: "))
    std_dev = float(input("Enter standard deviation: "))

    cognitive_bias = input("Apply cognitive bias? (yes/no): ").lower() == 'yes'
    memory_limitations = input("Apply memory limitations? (yes/no): ").lower() == 'yes'
    sensory_limitations = input("Apply sensory limitations? (yes/no): ").lower() == 'yes'
    biased_sampling = input("Apply biased sampling? (yes/no): ").lower() == 'yes'
    computational_limitations = input("Apply computational limitations? (yes/no): ").lower() == 'yes'

    # Generate the initial distribution based on user input
    distribution = generate_distribution(distribution_type, size, mean, std_dev)
    
    # Define a list of filter functions to apply
    filters = [
        apply_cognitive_bias,
        apply_memory_limitations,
        apply_sensory_limitations,
        apply_biased_sampling,
        apply_computational_limitations
    ]
    
    filtered_distribution = distribution
    for filter_func in filters:
        # Skip applying the biased sampling filter if not requested by the user
        if filter_func.__name__ == 'apply_biased_sampling' and not biased_sampling:
            continue
        # Apply the filter function to the distribution
        filtered_distribution = filter_func(filtered_distribution)

    # Plot both the original and filtered distributions
    plt.hist(filtered_distribution, bins=30, density=True, alpha=0.5, label='Filtered Distribution')
    plt.hist(distribution, bins=30, density=True, alpha=0.5, label='Original Distribution')
    plt.legend()
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Original and Filtered Distributions')
    plt.show()

if __name__ == "__main__":
    main()
