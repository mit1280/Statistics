from sklearn import linear_model
import numpy as np
xl = [95, 85, 80, 70, 60]
x = np.asarray(xl).reshape(-1, 1)
y = [85, 95, 70, 65,70]
lm = linear_model.LinearRegression()
lm.fit(x, y)
p=lm.predict(np.asarray([80]).reshape(-1,1))
print(round(p[0],3))
