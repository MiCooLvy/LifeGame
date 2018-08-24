import numpy as np

a = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
b = np.array([[1, 1, 0], [0, 0, 0], [0, 0, 1]])

c = a - b
print(c)
c = np.abs(c)
print(c)
s = np.sum(c)
print(s)
