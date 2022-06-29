import numpy as np

ar1 = np.array([[2,3,7],[8,7,3],[9,4,5]])
ar2 = np.array([[3,5,8],[6,1,2],[7,9,0]])


#sum of 2-d array element wise
print(ar1 + ar2)
#product of 2-d array element wise
print(ar1 * ar2)
#find sqaure root of each element in 2-d array
print(np.sqrt(ar1))


#find element according to conditions
print(np.where(ar1 > 5))
#count nonzero elements of array
print(np.count_nonzero(ar1))
#indexes of non zero indexes
print(np.nonzero(ar1))