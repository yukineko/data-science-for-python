import scipy.linalg as linalg
from scipy.optimize import minimize_scalar
import numpy as np

matrix = np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
print(linalg.det(matrix)) #行列式

print(linalg.inv(matrix)) #逆行列
print(matrix.dot(linalg.inv(matrix))) #逆行列の確認

eig_value, eig_vector = linalg.eig(matrix)
print("固有値:", eig_value)
print("固有ベクトル:\n", eig_vector)

def my_function(x):
    return x**2 + 2*x + 1

from scipy.optimize import newton
print(newton(my_function, 0)) #ニュートン法による最小化
print(minimize_scalar(my_function, method="Brent")) #スカラー最小化


q0 = np.array([1,2,3,1,3,2,3,1,2]).reshape(3, 3) #配列の形状を変更
print(q0)
print(linalg.det(q0))

eig, evec = linalg.eig(q0)
print(eig, evec)

def my_func2(x):
    return x**3 + 2*x + 1

print(newton(my_func2, 0)) #ニュートン法による最小化