def Reverse(arr):
    x = len(arr)
    print(x) 

    arr[2:8] = reversed(arr[2:8])
    print(arr)

arr = [2,8,4,3,1,0,7,9,10,23,11,25,27,89,95,54]
print(Reverse(arr))