n = int(input("Enter the size"))
arr = [None]*n

k = int(input("Enter the number of elements"))

for i in range(k):
    arr[i] = int(input())

def display():
    for i in range(len(arr)):
        print(arr[i])

display()
