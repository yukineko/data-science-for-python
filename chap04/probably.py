import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

dice_data = np.array([1,2,3,4,5,6])
print(np.random.choice(dice_data, 1))
calc_steps = 1000
dice_rolls = np.random.choice(dice_data, calc_steps)
print("Mean of dice rolls:", np.mean(dice_rolls))

for i in range(1,7):
    p = len(dice_rolls[dice_rolls==i]) / calc_steps
    print(f"Probability of rolling a {i}: {p:.3f}")


coin_data = np.array([1, 0])
coin_flips = np.random.choice(coin_data, 1000)
print("表", coin_flips[coin_flips==1].size / 1000)
print("裏", coin_flips[coin_flips==0].size / 1000)

print((0.99 * 0.001) / (0.99 * 0.001 + 0.03 * 0.999))

def uniform_distribution(x):
    prob_data = np.array([])
    for i in range(1,7):
        p = len(dice_rolls[dice_rolls==i]) / calc_steps
        prob_data = np.append(prob_data, p)

    print(prob_data)
    plt.bar(dice_data, prob_data)    
    plt.grid(True)
    plt.show()

def bernoulli_distribution():
    prob_be_data = np.array([])
    coin_data = np.array([1, 1, 1, 0, 0, 0, 0])
    for i in np.unique(coin_data):
        p = len(coin_data[coin_data==i]) / len(coin_data)
        prob_be_data = np.append(prob_be_data, p)
    plt.bar([0,1], prob_be_data, align='center')
    plt.xticks([0, 1], ['裏', '表'])
    plt.show()

# bernoulli_distribution()
def kernel_density():
    student_data_math = pd.read_csv("./student/student-mat.csv", sep=";")
    student_data_math.absences.plot(kind="kde", style="k--")
    student_data_math.absences.hist(density=True)
    plt.grid(True)
    plt.show()

