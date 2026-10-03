import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns

dataset = pd.read_csv('22.09.26_BostonHousing.csv')
dataset.head()
cols = ['lstat', 'indus', 'nox', 'rm', 'medv']
sns.pairplot(dataset[cols])

x = dataset[cols].values
y = dataset['medv']

regressor = LinearRegression
regressor.fit(x, y)
print(regressor.coef_)
print(regressor.intercept_)


c = np.zeros(6)
c[0] = regressor.intercent_
for i in range(5):
    c[i+1] = regressor.coef_[i]
F = np.zeros((len(y), 6))

for i in range(len(y)):
    F[i, 0] = 1
    for j in range(5):
        F[i, j+1] = x[i, j]

plt.plot(y, color = 'k', label = 'MedV')
plt.plot(F@c, '-o', color='red', label='Regression')
plt.tight_layout()
plt.grid()
plt.show()
#не все написала я чета все....