#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:21:41 2023

@author: molly
"""

import numpy as np
import matplotlib.pyplot as plt

def create_distribution(distribution_type, size, mean, std_dev):
    if distribution_type == 'gaussian' or distribution_type == 'normal':
        return np.random.normal(mean, std_dev, size)
    elif distribution_type == 'uniform':
        return np.random.uniform(mean, std_dev, size)
    elif distribution_type == 'exponential':
        return np.random.exponential(mean, size)
    elif distribution_type == 'poisson':
        return np.random.poisson(mean, size)
    elif distribution_type == 'lognormal':
        return np.random.lognormal(mean, std_dev, size)
    else:
        raise ValueError("Invalid distribution type")

# Example usage
distribution_type = 'uniform'
size = 1000
mean = 0
std_dev = 1

data = create_distribution(distribution_type, size, mean, std_dev)

# Plotting the distribution
plt.hist(data, bins=30, density=True, alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title(f'{distribution_type.capitalize()} Distribution (mean={mean}, std_dev={std_dev})')
plt.show()
