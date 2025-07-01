import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
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

#lognormal_distribution()

def kernel_density():
    student_data_math = pd.read_csv("./student/student-mat.csv", sep=";")
    student_data_math.absences.plot(kind="kde", style="k--")
    student_data_math.absences.hist(density=True)
    plt.grid(True)
    plt.show()


def practice1():
    np.random.seed(0)
    x = [np.random.normal(0, 1, 100).mean() for _ in range(10000)]
    plt.hist(x)
    plt.grid(True)
    plt.show()

def practice2():
    np.random.seed(0)
    x = [np.random.lognormal(0, 1, 100).mean() for _ in range(10000)]
    plt.hist(x)
    plt.grid(True)
    plt.show()

def practice3():
    student_data_math = pd.read_csv("./student/student-mat.csv", sep=";")
    student_data_math.G1.plot(kind="kde", style="k--")
    student_data_math.G1.hist(density=True)
    plt.grid(True)
    plt.show()

practice3()