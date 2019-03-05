import numpy as np
from sklearn import linear_model
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

# Create linear regression object
regr = linear_model.LinearRegression()

x = np.array([1,2,3,4,5,6])
x_train = x.reshape(-1, 1)
y_train = np.array([0.1778107, 0.01616287, 0.5425682, -0.2206135, -0.2392902, -0.0392704])

regr.fit(x_train,y_train)
y_pred = regr.predict(x_train)
plt.plot(x, y_pred, color='blue', linewidth=3)
plt.scatter(x, y_train,  color='black')

plt.show()
