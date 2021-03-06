import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3 #line function
reg = LinearRegression().fit(X, y)
reg.score(X, y) #determ. prediction
reg.coef_ # coefficients
reg.intercept_
reg.predict(np.array([[3, 5]]))
