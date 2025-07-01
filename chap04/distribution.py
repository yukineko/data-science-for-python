import numpy as np
import matplotlib.pyplot as plt

def binomial_distribution():
    # Generate a binomial distribution with n=30, p=0.5
    np.random.seed(0)
    x = np.random.binomial(30, 0.5, 1000)
    plt.hist(x)
    plt.grid(True)
    plt.show()    
    # Plot the histogram of the binomial distribution

#binomial_distribution()

def poisson_distribution():
    # Generate a Poisson distribution with lambda=5
    np.random.seed(0)
    x = np.random.poisson(7, 1000)
    plt.hist(x)
    plt.grid(True)
    plt.show()    
    # Plot the histogram of the Poisson distribution

#poisson_distribution()

def normal_dustribution():
    # Generate a normal distribution with mean=0, std=1
    np.random.seed(0)
    x = np.random.normal(5, 10, 1000)
    plt.hist(x)
    plt.grid(True)
    plt.show()    
    # Plot the histogram of the normal distribution

#normal_dustribution()

def lognormal_distribution():
    # Generate a log-normal distribution with mean=0, std=1
    np.random.seed(0)
    x = np.random.lognormal(30, 0.4, 1000)
    plt.hist(x)
    plt.grid(True)
    plt.show()    
    # Plot the histogram of the log-normal distribution

lognormal_distribution()

