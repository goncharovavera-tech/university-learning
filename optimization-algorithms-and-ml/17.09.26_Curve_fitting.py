import numpy as np
import matplotlib.pyplot as plt
import random as rnd

def f(x):
    return 2*np.log(x)*np.abs(np.cos(8+0.25*x)) #без абс гладкая функция

a, b, n = 7, 27, 1000
N = 30

X = np.linspace(a, b, N)
s = 1.2#случайность
Y = np.zeros(N)
for i in range(N):
    Y[i] = f(X[i]) + 2*s*rnd.random() - s #добавляем шума, как от приборов

x = np.linspace(a, b, n)
y = f(x)

m = 10#полином степени m-1, подгоняем g
Q = np.zeros((N, m))
for i in range(N):
    for j in range(m):
        Q[i, j] = X[i]**j

C = np.linalg.inv((Q.T)@Q)@(Q.T@Y)
print(C)

g = np.zeros(n)
for i in range(n):
    for j in range(m):
        g[i] += C[j]*x[i]**j


plt.scatter(X, Y, color = 'red')
plt.plot(x, g, color = 'green')
plt.plot(x, y, color = 'salmon')
plt.grid()
plt.show()