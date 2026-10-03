#Сортировка вставкой///Insertion
#Псевдокод:
#a(1), ... , a(n)
#for j = 2:n
#   x = a(j)
#   i = j-1
#   while i>0 and a(i) >= x:
#       a(i+1) = a(i)
#       i = i - 1
#   end
#   a(i+1) = x
#end

def Insertion(a):
    n = len(a)
    count = 0
    for j in range(1, n):
        count += 1
        x = a[j]
        i = j - 1
        count += 3 #для одной проверки
        while (i >= 0) and (a[i] >= x):
            a[i+1] = a[i]
            i -= 1
            #print(a[j], a[i])
            count += 2
        a[i+1] = x
        count += 1
    return count, a

a = [1, -1000, 666, -666, 56, 34, 1, 0.1, -5]
print(Insertion(a))



#Сортировка пузырьком///Booble sort
#Псевдокод:
#for i=1:n-1:
#   flag == 0
#   for j = 1:n-i:
#       if a(j) >= a(j+1):
#           x = a(j)    \
#                        | Swap(a(j), a(j+1))
#           a(j+1) = x  /
#           flag = 1
#       end
#   if flag == 0:
#       break
#   end
#end

def Booble(a): #он у нас сллишком хорошо работает
    n = len(a)
    count = 0
    for i in range(n-1):
        count += 1
        flag = False
        count += 1
        for j in range(n-1-i):
            count += 1 #j + проврка
            if a[j] >= a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
                count += 2 #swap - 1 и flag - 1
        count += 1 #опрерация для условия
        if flag == False:
            break
    return count, a

a_Booble = [1, -1000, 666, -666, 56, 34, 1, 0.1, -5]
print(Booble(a_Booble))

#Сортировка выбором///Selection Sort
#for i =1:n:
#   id = i
#   for j=i+1:n:
#       if a(j) <= a(id):
#           id = j
#       end
#   end
#   a(i), a(id) = a(id), a(i)
#end

def Selection(a):
    n = len(a)
    count = 0
    for i in range(n):
        k = i
        count += 2
        for j in range(i+1, n):
            count += 2
            if a[j] <= a[k]:
                k = j
                count += 1
        a[i], a[k] = a[k], a[i]
        count += 1
    return count, a

a_Sel = [1, -1000, 666, -666, 56, 34, 1, 0.1, -5]
print(Selection(a_Sel))

#У ВСЕХ ЭТИХ АЛГОРИТМОВ КВАДРАТИЧНАЯ ТРУДОЕМКОСТЬ

###Время работы - число операций

import numpy as np
import matplotlib.pyplot as plt
import time
#QT * Q * c = QT * Y
N = 100
M = 20
n = np.zeros(M)
TI = np.zeros(M)
TB = np.zeros(M)
TS = np.zeros(M)
for i in range(M):
    n[i] = N*(i+1)
    a = np.random.rand(N*(i+1))
    print(len(a))
    start_time = time.time()
    Insertion(a)
    TI[i] = time.time() - start_time
    #TI[i], a = Insertion(a)
    start_time = time.time()
    Booble(a)
    TB[i] = time.time() - start_time
    #TB[i], a = Booble(a)
    start_time = time.time()
    Selection(a)
    TS[i] = time.time() - start_time
    #TS[i], a = Selection(a)
Q = np.zeros((M, 3))
for i in range(M):
    for j in range(3):
        Q[i, j] = n[i]**j #получаем степени n-ок
cI = np.zeros((3, 1))
cS = np.zeros((3, 1))
cI = np.linalg.inv(Q.T@Q)@(Q.T@TI)
cS = np.linalg.inv(Q.T@Q)@(Q.T@TS)
print(np.linalg.solve(Q.T@Q, Q.T@TI))
print(cI)
Tai = np.zeros(M)
Tai = cI[0] + cI[1]*n + cI[2]*n**2
Tas = np.zeros(M)
Tas = cS[0] + cS[1]*n + cS[2]*n**2
plt.plot(n, Tai, color = 'blue')
plt.plot(n, Tas, color = 'orange')
plt.scatter(n, TI, color = 'cyan')
plt.scatter(n, TB, color = 'magenta')
plt.scatter(n, TS, color = 'yellow')
plt.grid() #сетка
plt.show() #выводим график