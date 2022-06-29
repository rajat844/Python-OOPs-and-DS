import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 1, 0]])
print(x)
# sum of all columns
print(x.sum(axis=0))
# sum of all rows
print(x.sum(axis=1))
# transpose of array
print(x.T)
# live raval we can use flat
print(x.ravel())
# but it will provide its iterator and can be used in for loops
for y in x.flat:
    print(y)

# find number of dimensions of array
print(x.ndim)
# amount of memory used by array
print(x.nbytes)

one = np.array([2, 3, 4, 7, 2, 9])
# print maximum element index of an array
print(one.argmax())
# print minimum element index of an array
print(one.argmin())
# print elements sorted indexwise
print(one.argsort())

# in 2dimension arrays

# max element index of 2-d array after raveling it
print(x.argmax())
# max element index of 2-d array in each column
print(x.argmax(axis=0))
# max element index of 2-d arrat in each row
print(x.argmax(axis=1))
