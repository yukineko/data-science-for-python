import numpy as np
from scipy import interpolate

import scipy.linalg as linalg
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x ** 2/5.0)

def show_plot(x, y, f):
    plt.plot(x, y, 'o', label='data points')
    plt.plot(x, f(x), '-')
    plt.grid(True)
    plt.show()

def interp_func(x, y, x_new):
    f = interpolate.interp1d(x, y, kind='linear')
    plt.plot(x, y, 'o', label='data points')
    plt.plot(x, f(x), '-')
    plt.grid(True)
    plt.show()

#interp_func(x, y, x)


def spline_3d(x, y):
    f = interpolate.interp1d(x, y, kind='linear')
    f2 = interpolate.interp1d(x, y, kind='cubic')
    xnew  = np.linspace(0, 10, num=30, endpoint=True)
    plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--', label='data points')
    plt.legend(['data', 'linear', 'cubic'], loc='best')
    plt.grid(True)
    plt.show()

#spline_3d(x, y)

def practice():
    x = np.linspace(0, 10, num=11, endpoint=True)
    y = np.cos(-x ** 2/5.0)
    f = interpolate.interp1d(x, y, kind='linear')
    f2 = interpolate.interp1d(x, y, kind='quadratic')
    f3 = interpolate.interp1d(x, y, kind='cubic')

    plt.plot(x, y, 'o',f(x), '-', f2(x), '--', f3(x), 'r--', label='data points')
    plt.grid(True)
    plt.show()

#practice()

def svd():
    x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    U, s, Vs = linalg.svd(x)
    m, n = x.shape
    S = linalg.diagsvd(s, m, n)
    print('U.S.V* + \n', U @ S @ Vs)

#svd()

def lu():
    A = np.identity(5)
    A[0,:] = 1
    A[:,0] = 1
    A[0,0]= 5
    print(A)
    (LU, piv) = linalg.lu_factor(A)
    L = np.identity(5) + np.tril(LU, -1)
    U = np.triu(LU)
    P = np.identity(5)[piv]
    b = np.ones(5)
    x = linalg.lu_solve((LU, piv), b)
    # print('P:\n', P)
    # print('L:\n', L)
    # print('U:\n', U)
    print('x:\n', x)

#lu()

def colesky():
    A = np.array([[7, -1, 0, 1], 
                  [-1, 9, -2, 2], 
                  [0, -2, 8, -3],
                  [1, 2, -3, 10]])
    B = np.array([5, 20, 0, 20])
    L = linalg.cholesky(A)
    print('L:\n', L)
    t = linalg.solve(L.T.conj(), B)
    x = linalg.solve(L, t)
    print('x:\n', x)
#colesky()

def nmf():
    X = np.array([[1, 2, 3, 4, 5], 
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15]])
    model = NMF(n_components=2)
    W = model.fit_transform(X)
    H = model.components_
    print('W:\n', W)
    print('H:\n', H)
    print('Reconstructed X:\n', np.dot(W, H))

#nmf()

def practice2_1():
    B = np.array([[1, 2, 3], 
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]])
    U, s, Vs = linalg.svd(B)
    m, n = B.shape
    S = linalg.diagsvd(s, m, n)
    print('U:\n', U)
    print('S:\n', S)
    print('Vs:\n', Vs)
    print('U.S.V* + \n', U @ S @ Vs)
#practice2_1()

def practice2_2():
    A = np.identity(5)
    A[0,:] = 1
    A[:,0] = 1
    A[0,0]= 3
    b = np.ones(5)
    (LU, piv) = linalg.lu_factor(A)
    U = np.triu(LU)
    L = np.identity(5) + np.tril(LU, -1)
    P = np.identity(5)[piv]
    x = linalg.lu_solve((LU, piv), b)
    print('P:\n', P)
    print('L:\n', L)
    print('U:\n', U)
    print('x:\n', x)
#practice2_2()