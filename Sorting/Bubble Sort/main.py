def bubble(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

x = list(map(int,input().strip().split()))
print(bubble(x))