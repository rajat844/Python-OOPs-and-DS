def selection(arr):
    n = len(arr)

    for i in range(n):
        k = i
        for j in range(i,n):
            if arr[j] < arr[k]:
                k = j
        arr[i],arr[k] = arr[k],arr[i]

    return arr
x = list(map(int,input().strip().split()))
print(selection(x))