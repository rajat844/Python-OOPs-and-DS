from numpy import insert


def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        j = i-1
        x = arr[i]
        while j > -1 and arr[j] > x:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x

    return arr

x = list(map(int,input().strip().split()))
print(insertion(x))