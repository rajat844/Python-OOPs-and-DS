import numpy as np
#array of zeros
z = np.zeros((2,5))

#array of range 
rng = np.arange(2,5)

#equal spaces array in range
lspace = np.linspace(0,50,6)

#creating empty array of size
emp = np.empty((4,3))

#creating empty array like another array
empLike = np.empty_like(rng)

#creating identity matrix of size
iden = np.identity(6)

#create matrix of range of numbers
rnc = np.arange(0,9)
#divide matrix into numbers of rows and colums
rnc = rnc.reshape(3,3)
#array from matrix form to list form
rncStraight = rnc.ravel()

#
print(z)
print(rng)
print(lspace)
print(emp)
print(empLike)
print(iden)
print(rnc)
print(rncStraight )