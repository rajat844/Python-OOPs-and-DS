import imp
import pandas as pd
import imp
import numpy as np

dict1 = {
    "name" : ['rajat','harry','rohan','shubh'],
    "marks": [92,34,24,17],
    "city": ['East Delhi','kolkata','bareily','agra']
}

df = pd.DataFrame(dict1)
#create excel sheet withou index
df.to_csv('dict.csv',index= False)
#create excel sheet with index
df.to_csv('indexedDict.csv')
#to show first n rows
print(df.head(2))
#to show last n rows
print(df.tail(3))
#find all basic data of nurical rows
print(df.describe())
#extract data from the dataframe
print(df['marks'][0])
#change data in data frame
df['marks'][3] = 54
print(df)
df.to_csv('indexedDict.csv')
