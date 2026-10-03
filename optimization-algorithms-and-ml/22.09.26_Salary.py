import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv('22.09.26_Salary.csv')
dataset.head()
X = dataset[['YearsExperience']].values
Y = dataset[['Salary']].values



###делаем сами
F = np.zeros((30, 2))
for i in range(30):
    F[i, 0] = 1
    F[i, 1] = X[i, 0]
c = np.linalg.solve(F.T@F, F.T@Y)
#print(c[0] + c[1]*9)

regressor = LinearRegression()
regressor.fit(X, Y)
print(c)
print()
print(regressor.coef_)
print(regressor.intercept_)


M = 500
x = np.linspace(min(X), max(X), M)
y = regressor.predict(x)

plt.scatter(X, Y, color='cyan')
plt.plot(X, c[0]+c[1]*X, color = 'blue')
plt.plot(x, y, color = 'darkturquoise')
plt.grid()
plt.show()
