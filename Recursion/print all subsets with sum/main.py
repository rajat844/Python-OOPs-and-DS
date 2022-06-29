def allSubsets(arr,x):
    ans = []
    n = len(arr)

    def helper(index,s):
        if index == n:
            if sum(s) == x:
                temp = []
                for i in s:
                    temp.append(i)
                ans.append(temp)
            return 
        s.append(arr[index])
        helper(index+1,s)
        s.pop()
        helper(index+1,s)
    
    helper(0,[])
    return ans

arr = list(map(int,input().strip().split()))
x = int(input())
p = allSubsets(arr,x)
print(p)