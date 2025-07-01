import numpy as np
import matplotlib.pyplot as plt

def large_number():
    calc_times = 1000
    sample_array = np.array([1,2,3,4,5,6])
    number_cnt = np.arange(1, calc_times + 1)

    for i in range(4):
        p = np.random.choice(sample_array, calc_times).cumsum()
        plt.plot(p / number_cnt)
        plt.grid(True)
        plt.show()

def function_central_theory(N=3):
    sample_array = np.array([1,2,3,4,5,6])
    number_cnt = np.arange(1, N + 1) * 1.0

    mean_array = np.array([])

    for i in range(1000):
        cum_variables = np.random.choice(sample_array, N).cumsum()* 1.0
        mean_array = np.append(mean_array, cum_variables[N-1] / N)
    plt.hist(mean_array)
    plt.grid(True)
    plt.show()

#function_central_theory()
def chi2_theory():
    for df, c in zip([2,10,60], ['b', 'g', 'r']):
        x = np.random.chisquare(df, 1000)
        print(x)
        plt.plot(x, 20, color=c)
        plt.grid(True)
        plt.show()

chi2_theory()