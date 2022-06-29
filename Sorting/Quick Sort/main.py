def quick(arr):
    def part(start, end):
        i = start- 1
        pivot = arr[end]

        for j in range(start,end):
            if arr[j] <= pivot:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
        
        arr[i+1],arr[end] = arr[end],arr[i+1]
        return i+1

    def quickSort(start, end):
        if start < end:
            p = part(start, end)
            quickSort(start, p-1)
            quickSort(p+1, end)

    quickSort(0, len(arr) - 1)
    return arr


x = list(map(int, input().strip().split()))
print(quick(x))
