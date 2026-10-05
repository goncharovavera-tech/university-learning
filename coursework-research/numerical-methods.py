import numpy as np
import matplotlib.pyplot as plt

a_t, b_t, N_t = 0, 20, 150
tau = np.abs(a_t - b_t)/N_t
a_h, b_h, N_h = -50, 51, 50
h = np.abs(a_h- b_h)/N_h
c = 1.5
K = c*tau/h

print(f"tau = {tau}, h = {h}, c = {c}")

X = np.linspace(a_h, b_h, N_h)
T = np.linspace(a_t, b_t, N_t)

def f(x):# буду использывать Гауссовую функцию
    a = 1
    b = -20
    c = 5
    return a * np.exp(-(x-b)**2 / (2 * c**2))

def dif_scheme_1(X, T):#по учебнику 3.3 уголок смотри вправо вниз
    u = np.zeros((N_t, N_h))
    u[0, :] = f(X)
    for k in range(len(T) - 1):
        for n in range(1, len(X)):
            u[k+1, n] = u[k, n] - K*(u[k, n] - u[k, n-1])
    return u


def dif_scheme_2(X, T):#по учебнику 3.5 уголок смотри вправо вверх
    u = np.zeros((N_t, N_h))
    u[0, :] = f(X)
    for k in range(len(T) - 1):
        for n in range(1, len(X)):
            u[k+1, n] = (u[k, n] + K*u[k+1, n-1])/(1+K)
    return u

def dif_scheme_3(X, T):#по учебнику 3.6 уголок смотри влево вниз
    u = np.zeros((N_t, N_h))
    u[0, :] = f(X)
    for k in range(len(T) - 1):
        for n in range(len(X)-1):
            u[k+1, n] = u[k, n] - K*(u[k, n+1] - u[k, n])
        u[k + 1, -1] = (u[k, -2] - K*(u[k, -1] - u[k, -2]))
                    #химичу чтобы заполнить послдений столбец по T
                    #len(X)-1 - послдениц эелемент из X
                    #len(X)-2 - предпослдениц эелемент из X
    return u

if K <= 1:
    print(f'Схема устойчива: Условие Куранта-Фридрикса {K} <= 1')
else:
    print(f'Cхема неустойчива: Условие Куранта-Фридрикса {K} > 1')

plt.figure()
u_1 = dif_scheme_1(X, T)
plt.title("Угол право вниз")
plt.xlabel("x")
plt.ylabel("t")
plt.plot(X, u_1[-1, :], color = 'blue')
plt.plot(X, f(X - c*b_t), color = 'lightblue')
plt.ylim(-0.2, 1.2)
plt.grid()


plt.figure()
u_2 = dif_scheme_2(X, T)
plt.title("Угол вправо вверх")
plt.xlabel("x")
plt.ylabel("t")
plt.plot(X, u_2[-1, :], color = 'red')
plt.plot(X, f(X - c*b_t), color = 'salmon')
plt.ylim(-0.2, 1.2)
plt.grid()

plt.figure()
u_3 = dif_scheme_3(X, T)
plt.title("Угол влево вниз")
plt.xlabel("x")
plt.ylabel("t")
plt.plot(X, u_3[-1, :], color = 'orange')
plt.plot(X, f(X - c*b_t), color = 'yellow')
plt.ylim(-0.2, 1.2)
plt.grid()

plt.show()