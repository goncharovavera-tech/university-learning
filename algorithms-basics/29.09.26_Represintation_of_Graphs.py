#надо вспомнить матрицу смежности графа вспомни
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

def ConvertMatrixToList(a):
    adjList = defaultdict(list)#правила приличия что он создает хз
    #dict1 = dict()
    print(adjList)
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] != 0:
                adjList[i].append(j)
                #dict1[i] = dict1.get(i, []) + [j]
    #print(dict1)
    return adjList


A = np.ones((6, 6))
for i in range(6):#там картинка в ней этот граф
    A[i][i] = 0
A[0][4] = 0
A[4][0] = 0
A[1][5] = 0
A[5][1] = 0
A[2][3] = 0
A[3][2] = 0

AdjList = ConvertMatrixToList(A)
print("AdjList:", AdjList)

for i in AdjList:
    print(i, end=":")
    for j in AdjList[i]:
        print(' ->', j, end="")
    print()

#Генерим случайную матрицу смежности
n, m = 4, 4
adj_matrix = np.zeros((n, n), dtype= int)
#массива всех возможных ребер для графа на вершинах n
all_edges = np.array([(i, j) for i in range(n) for j in range(i+1, n)])

print("all_edges=", all_edges)
print(all_edges[1])
edges = all_edges[np.random.choice(len(all_edges), size=m, replace=False)]

for i, j in edges:
    adj_matrix[i, j] = 1
    adj_matrix[j, i] = 1
print(adj_matrix)


'''import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
nodes = [0, 1, 2, 3, 4, 5]
edges = [(0, 1), (0, 2), (0, 3), (0, 5), (1, 2), (1, 3), (1, 4), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
#edges = [(0, 1), (0, 2), (1, 2)]
G.add_nodes_from(nodes)
G.add_edges_from(edges)
#pos = nx.circular_layout(G)
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
#nx.draw(G)
plt.show()

print(G.nodes())
print(G.edges())

Ag = nx.from_numpy_array(G)
print(Ag)

G1 = nx.from_numpy_array(A)
#G1.edges(data=True)
nx.draw(pos, with_labels=True, font_weight='bold')
plt.show()
'''''''#эта штука у меня не рабоотал попросила нейронку исправить

# ИСПРАВЛЕНО: получаем матрицу из графа (to_numpy_array)
A = nx.to_numpy_array(G)
print("\nМатрица смежности:\n", A)

# ИСПРАВЛЕНО: создаем новый граф из матрицы A
G1 = nx.from_numpy_array(A)

# --- РИСУЕМ ВТОРОЙ ГРАФ ---
plt.figure(2)  # Создаем второе окно
# ИСПРАВЛЕНО: первым аргументом передаем граф G1, а не pos
pos1 = nx.kamada_kawai_layout(G)
nx.draw(G1, pos1, with_labels=True, font_weight="bold", node_color="orange")
plt.show()


plt.figure(3)
n = 8#кол-во вершин
p = 1#вероятость создания ребра между любой парой вершин
G = nx.generators.random_graphs.gnp_random_graph(n, p)
nx.draw(G)
plt.show()'''

#ОБХОД В ГЛУБИНУ
import time
def DFS(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            DFS(visited, graph, neighbour)
def DFS_count(visited, graph, node, count):
    count += 1
    if node not in visited:
        print(node)
        visited.append(node)
        count += 1
        for neighbour in graph[node]:
            count += 1
            count = DFS_count(visited, graph, neighbour, count)
    return count

visited = []
DFS(visited, AdjList, 4)
print(visited)

N = 50
n = np.linspace(200, 00, N)
print(n)

V = np.zeros(N)
E = np.zeros(N)
T = np.zeros(N)

for i in range(N):
    V[i] = n[i]
    E[i] = 0.5*(V[i]*(V[i]-1))
    A = np.ones((int(n[i]), int(n[i])))
    for j in range(int(n[i])):
        A[j][j] = 0
    AdjList = ConvertMatrixToList(A)
    visited = []
    start_time = time.time()
    count = DFS_count(visited, AdjList, 0, 0)
    #T[i] = count
    T[i] = time.time() - start_time

plt.scatter(V, T)
plt.show()