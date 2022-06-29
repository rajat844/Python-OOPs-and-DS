class Stack :
    def __init__(self,size):
        self.s = []
        self.size = size
    
    def push(self,ele):
        if (len(self.s) < self.size):
            self.s.append(ele)
        else:
            print("stack is full")
    
    def pop(self)->int:
        del self.s[0]
    
    def peek(self,index)->int:
        if len(self.s) >= index:
            return self.s[index-1]
        
        return None
    
    def stackTop(self)->int:
        return self.s[0]
    
    def isEmpty(self)->bool:
        if len(self.s) > 0:
            return False
        else :
            return True
        
    def isFull(self)->bool:
        if len(self.s) == self.size:
            return True
        else :
            return False



st1 = Stack(5)
st1.push(1)



    

