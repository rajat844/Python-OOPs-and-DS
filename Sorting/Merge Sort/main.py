from turtle import left, right


def merge(arr):
    n = len(arr)

    def mergeaction(low, mid, high):
        temp = []
        i = low
        j = mid

        while i <= mid-1 and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
                

        while i <= mid - 1:
            temp.append(arr[i])
            i += 1

        while j <= high:
            temp.append(arr[j])
            j += 1

        a = 0
        for i in range(low, high+1):
            arr[i] = temp[a]
            a += 1

    def mergeSort(low, high):
        while low < high:
            mid = (low + high)//2
            mergeSort(low, mid)
            mergeSort(mid+1, high)

            mergeaction(low, mid+1, high)

    mergeSort(0, n-1)
    return arr


x = list(map(int, input().strip().split()))
print(merge(x))
