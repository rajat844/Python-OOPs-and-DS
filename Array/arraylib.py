import array

lst = [1, 2, 3, 4, 5]

a = array.array('i', lst)

a.pop(1)

for i in range(len(a)):
    print(a[i])
