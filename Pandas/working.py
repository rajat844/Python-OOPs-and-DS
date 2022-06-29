from gettext import npgettext
from hashlib import new
import pandas as pd
import numpy as np

#create series in pandas
ser = pd.Series(np.random.rand(34))
print(ser)
#create dataframe in pandas
newdf = pd.DataFrame(np.random.rand(334,9),index = np.arange(334))
print(newdf.head())
print(type(newdf))

#convert to numpy
newdf[0][0] = 'rajat'
x = newdf.to_numpy()
print(x)

#define datatype of each column in dataframe
print(newdf.dtypes)

#all rows of dataframe
print(newdf.index)
#all colums of dataframe
print(newdf.columns)

#transpose of dataframe
print(newdf.T)

#sort according to index
print(newdf.sort_index(axis = 0,ascending= False))
print(newdf.sort_index(axis= 1,ascending= False))

#change element without a warning
newdf.loc[0,1] = 7373

#change columns name of the dataframe
newdf.columns = list("ABCDEFGHI")
print(newdf.head())

#drop a column from the dataFrame
newdf = newdf.drop('I',axis = 1)
print(newdf.head())
newdf.drop('H',axis = 1,inplace= True)
#drop a row from the dataframe
newdf = newdf.drop(0,axis = 0)
print(newdf.head())
newdf.drop(1,inplace = True)

#get specific rows and columns from the datafrome
print(newdf.loc[[2,3],['C','D']])

#to get all rows or columns is ':'
print(newdf.loc[:,['A','B']])

#filter using certain contion
print(newdf.loc[(newdf['A'] < 0.2)])

#to retrive elements in index instead of column name
print(newdf.iloc[[2],[3,4]])

#reset indexing of datafrome
newdf.reset_index(drop= True,inplace=True)
print(newdf.head())
