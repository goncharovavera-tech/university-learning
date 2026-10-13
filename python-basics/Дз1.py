''' ДЗ 1'''

#Задание 3
print('Задание 3')
var1, var2 = int(input()), int(input())
if var1 < var2:
    print(var1)
else:
    print(var2)

#Задание 4
print('Задание 4')
var1, var2, var3 = int(input()), int(input()), int(input())
minn = 99999
if var1<minn:
    minn = var1
if var2 < minn:
    minn = var2
if var3 < minn:
    minn = var3
print(minn)


#Задание 5
print('Задание 5')
vars= [int(i) for i in input().split()]
dt = dict()
for i in vars:
  dt[i] = dt.get(i, 0) + 1
print(len(dt))

#Задание 6
print('Задание 6')
print(sum(range(10)))

#Задание 8
print('Задание 8')
n = int(input())
for i in range(n):
  print(*range(i+1))

#Задание 9
print('Задание 9')
#n = int(input())
n = 6
for i in range(n):
  if i < n:
    print(' '*(n - i), end='')
   # print('*')
  print(*range(i+1))

#Задание 7
print('Задание 7')
vars = [int(i) for i in input().split()]
print(vars.count(0))