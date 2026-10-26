#Номер 1
print('Номер 1')
s = input().split()
for i in range(len(s)):
    s[i] = s[i].capitalize()
print(' '.join(s))

#Номер 2
print('Номер 2')
list1 = input().split()
list2 = []
for i in range(1, len(list1), 2):
    list2.append(list1[i])
print(*list2)

#Номер 3
print('Номер 3')
list1 = [int(i) for i in input().split()]
list2 = []
for i in range(1, len(list1)):
    if list1[i] > list1[i-1]:
        list2.append(list1[i])
print(*list2)

#Номер 4
print('Номер 4')
dt = {'cat': 1, 'dog': 4}
def func(key):
    global dt
    return dt[key]
print(func('cat'))

#Номер 5
set1 = set(input())
set2 = set(input())
print(set1.issubset(set2))

