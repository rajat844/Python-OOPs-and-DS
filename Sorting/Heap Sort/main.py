def heapify(nums,start,end):
    largest = start
    left = 2*start + 1
    right = 2*start + 2

    if left < end and nums[left] > nums[largest]:
        largest = left
    
    if right < end and nums[right] > nums[largest]:
        largest = right
    
    if largest != start:
        nums[largest],nums[start] = nums[start],nums[largest]
        heapify(nums,largest,end)

def sort(nums):
    n = len(nums)
    for i in range((n//2) -1 ,-1,-1):
        heapify(nums,i,n)

    for i in range(n-1,0,-1):
        nums[i],nums[0] = nums[0],nums[i]
        heapify(nums,0,i)


nums = list(map(int,input().strip().split()))
sort(nums)
print(nums)