from scipy import integrate
from scipy.optimize import fsolve, minimize
import scipy.linalg as linalg
import numpy as np
import math
import matplotlib.pyplot as plt
def calcPi(x):
    return 4/(1+x**2)

def integratePi():
    print(integrate.quad(calcPi, 0, 1))

integratePi()

print(integrate.quad(np.sin, 0, math.pi/2))

def l(n):
    return integrate.dblquad(
        lambda t, x: np.exp(-x*t)/t**n,0,np.inf, 
        lambda x:1, lambda s: np.inf)[0]
print(l(1))
print(l(2))
print(l(3))

def f(x):
    return 2 * x ** 2 + 2* x - 10
def fsolve_example():
    x = np.linspace(-10, 10, 100)
    plt.plot(x, f(x), label='f(x)')
    plt.plot(x, np.zeros(len(x)))
    plt.grid(True)
    plt.show()

x = fsolve(f, 2)
print(x)

def objective(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return x1 * x4 * (x1 + x2 + x3) + x3

def constraint2(x):
    sum_sq = 40
    for i in range(4):
        sum_sq = sum_sq -x[i] ** 2
    return sum_sq

def constraint1(x):
    return x[0] * x[1] * x[2] * x[3] - 25.0

x0 = [1,5,5,1]
#print(objective(x0))
b = (1.0,5.0)
bnds = (b,b,b,b)
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint1}
cons = [con1, con2]
sol = minimize(objective, x0, method='SLSQP', bounds=bnds,constraints=cons)
print(sol)
print(sol.fun)
print(sol.x)

def practice517():
    def f(x):
        return 5 * x - 10
    x = np.linspace(0, 5, 100)
    # plt.plot(x, f(x), label='f(x)')
    # plt.plot(x, np.zeros(len(x)))
    # plt.grid(True)
    # plt.show()
    
    x = fsolve(f, 2)
    print(x)

#practice517()

def practice518():
    def f(x):
        return x ** 3 - 2 * x ** 2 - 11 * x + 12
    # x = np.linspace(-5, 5, 100)
    # plt.plot(x, f(x), label='f(x)')
    # plt.plot(x, np.zeros(len(x)))
    # plt.grid(True)
    # plt.show()
    
    x = fsolve(f, 1)
    print(x)

#practice518()

def practice_51():
    A = np.array([
        [5,1,0,1],
        [1,9,-5,7],
        [0,-5,8,-3],
        [1,7,-3,10]
    ])
    B = np.array([2,10,5,10])
    x = linalg.cholesky(A)
    print('L:\n', x)
    t = linalg.solve(x.T.conj(), B)
    x = linalg.solve(x, t)
    print('x:\n', x)

#practice_51()

def practice_52():
    r = integrate.dblquad(lambda x, y: 1/(np.sqrt(x+y) * (1+x+y)**2), 0, 1,
                          lambda x: 0, lambda x: 1-x)
    print(r)

#practice_52()

def minfx(x):
    return x ** 2 + 1
    
def constraintfx(x):
    return x + 1

con1 = (
    {'type': 'ineq', 'fun': constraintfx}
    )
x = -1
sol = minimize(minfx, x0=x, constraints=con1, method='SLSQP')
print(sol)