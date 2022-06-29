import array

a = array.array("i")

n = int(input("Enter the size: "))

for i in range(n):
    x = int(input())
    a.append(x)

def binarySearch(k):
    for i in range(len(a)):
        if k == a[i]:
            return i
    
    return -1

k = int(input())
print(binarySearch(k))

