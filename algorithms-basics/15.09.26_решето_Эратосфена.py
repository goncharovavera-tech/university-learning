#15.09.26
#Решето Эратосфена, мы выводим некоторое нат число n
# и алгоритм выдает нам все простые числа до этого числа
#рука: выписываем все числа подряд до n влючитальено
# и начиная с первого рекурентно вычерскивае
# все числа которые без остатка делятся на числа из списка
import numpy as np


#идея: зададим массив, идексация от 0 до n; перебираем
#все числа начиная от 2 и последовательно зануляем кратные
#в конце убираем все нули

def EratosphenSeive(n, count = 0):
    primes = [i for i in range(n+1)]
    primes[1] = 0
    i = 2
    while i <= n:
        count += 1
        if primes[i] != 0:
            j = 2*i #смотрим кратные числа
            count += 1
            while j <= n:
                primes[j] = 0 #первой шаг
                j += i #второй шаг
                count += 2
        i += 1
    primes = [i for i in primes if i != 0]
    return count, primes

#надо подтвердить теоритическую трудоемкость О(n*ln(ln(n)))
#эмпиритический анализ алгоритма:
#1) генерируем данные при последовательно увеличивающемся n
#2) при каждом ni мы изимеряем время Т(число операций/время работы)
#в этом случае будет число операций
#3) приближаем полученную зависемость,задаваемую точками (ni, Ti), i = 1, n
#аналитической зависемостью подтверждающей теоритическую оценку

#T(n) = O(n*ln(ln(n))): T(n) <= C*n*ln(ln(n))
#на графике точки будут C1*n*ln(ln(n)) + C2
#C1, C2 определяем методом наименьших квадратов

import numpy as np
a, b = 100, 10000
N = [int(i) for i in np.linspace(a, b, int(b/a))]
n = len(N)
print(n, N)
#print(EratosphenSeive(int(input())))

import matplotlib.pyplot as plt
T = np.zeros(n) #N = [int(i) for i in np.linspace(a, b, int(b/a))]
for i in range(n):
    T[i], primes = EratosphenSeive(N[i])

plt.scatter(N, T, color= 'blue') #точки и их цвет



#идея метода наименьших квадрантов:
#стоится f(n) = g(n, C1, C2) смотрим отклонения в точках между
# предполагаемой функцией и экспеременатльными даннфми,
# возводим их в квадрат и минимизируем
# 1/k * sum[по n от i до k](g(ni, C1, C2) - Ti)**2 -> min по C1, C2
# эту функицю обзовем F(C1, C2)
#F = matr[1      n1*ln(ln(n1)         dim(F) = k * 2
#         ...    ...                  C1*f1(n) + C2*f0(n)
#         1      nk*ln(ln(nk)]
#тогда:
#F = matr[f0(n1)  f1(n1)
#         ...     ...
#         f0(nk)  f1(n1)]
#Преобразу T1(n) = C1 + C2*n*ln(ln(n))
#C1, C2-? Из СЛАУ:            С = matr[C1, C2]**T; T = [T1, ... , Tk]**T
#F**T * F * C = F ** T * T; роде бы так мб я не так переписала с доски

F = np.zeros((n, 2))
for i in range(n):
    F[i, 0] = 1
    F[i, 1] = N[i] *np.log(np.log(N[i]))

C = np.linalg.inv(np.transpose(F)@F)@(np.transpose(F)@T) #@ - матричное умножение
                                #в место np.transpose можно писать просто .T
#проверяем С
t = np.zeros(n)
for i in range(n):
    t[i] = C[0]+C[1]*N[i]*np.log(np.log(N[i]))


plt.plot(N, t, color= 'red')#сам график и его цвет
plt.grid() #сетка
plt.show() #выводим график




