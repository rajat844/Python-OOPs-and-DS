#array creation from python objects
import numpy as np 
#creating as int
listarray = np.array([[1,2,3],[5,6,7],[0,3,1]])

#creating as object
#listarray = np.array({32,6,15})
#print array
print(listarray)
#array shape
print(listarray.shape)
#array size
print(listarray.size)
#array type
print(listarray.dtype)