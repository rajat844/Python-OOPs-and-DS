def f(i,j):
    if i>=j:
        return 
    x = arr[i]
    arr[i] = arr[j]
    arr[j] = x
    f(i+1,j-1)


arr = list(map(int,input().strip().split()))
f(0,len(arr)-1)
print(arr)