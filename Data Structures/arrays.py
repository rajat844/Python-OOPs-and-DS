from hashlib import new


new_list = [1,2,3]
result = new_list[0]

if 1 in new_list : print(True)

for n in new_list:
    if n == 1:
        print (True)
        break


#Insert : list.insert(index,value)
#Append : list.append(value)
#multipleAppend : list.extend([arr of elements])
#delete : del list(start position, end position)
#search : if val in list 
