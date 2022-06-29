import numpy as np

myarr = np.array([[3,7,32,7]],np.int64)
myarr[0,1] = 45
print(myarr)
print(myarr[0,1])
print(myarr.shape)
print(myarr.dtype)
