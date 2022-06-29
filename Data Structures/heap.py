class Heap:
    def __init__(self) -> None:
        self.st = []


    def create(self,nums)->None:
        for i in range(len(nums)):
            self.insert(nums[i])

    def print(self):
        print(self.st)    
    
    def insert(self,val) -> None:
        self.st.append(val)
        n = len(self.st) - 1
        while (n > 0 and  val > self.st[n//2]):
            self.st[n] = self.st[n//2]
            n = n//2
        self.st[n] = val

    def delete(self):
        if len(self.st) == 1:
            return self.st.pop()
            
        x = self.st[0]
        self.st[0] = self.st.pop() 
        n = len(self.st)
        i = 0
        j = 2*i+ 1

        while j < n-1:
            if self.st[j+1] > self.st[j]:
                j = j+1
            
            if self.st[i] < self.st[j]:
                self.st[j],self.st[i] = self.st[i],self.st[j]
                i = j
                j = 2*i + 1
            else:
                break
        return x
    
    def heapSort(self):
        ans = []
        n = len(self.st)
        for i in range(n):
            ans.append(self.delete())
        
        return ans


heap = Heap()
nums = [40,20,30,25,35,41,10,15]
heap.create(nums)
heap.insert(50)
print(heap.heapSort())
