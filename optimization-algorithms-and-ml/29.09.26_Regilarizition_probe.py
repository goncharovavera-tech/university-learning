import numpy as np
import matplotlib.pyplot as plt

n = 100
A = np.zeros((n, n))
b = np.ones(n)

delta = 0
#вносим в вектор b случайный шум
for i in range(n):
    b[i] += 2*delta*np.random.rand() - delta

for i in range(n):
    for j in range(n):
        A[i, j] = 1/((i+1)+(j+1)-1)

x1 = np.linalg.inv(A)@b
x2 = np.linalg.solve(A, b)

r1 = np.linalg.norm(A@x1-b)
r2 = np.linalg.norm(A@x2-b)

print(r1)
print(r2)

alp = 1
x_alp = np.linalg.inv(A.T@A + alp*np.identity(n))@(A.T@b)

r_alp = np.linalg.norm(A@x_alp-b)
print(r_alp)

plt.figure(1)
plt.plot(x1, color = 'black')
plt.plot(x_alp, color = 'red')
plt.show()

plt.figure(2)
plt.plot(x_alp, color = 'blue')
plt.show()

