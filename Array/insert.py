import array

lst = [1,2,3,4,5]

a = array.array("i",lst)

t = int(input())
a.append(t)

print(a)