class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        new_node = Node(val)

    def pop(self):
        if self.head is not None:
            self.head = self.head.next


class Stack:

    def __init__ (self,size):
        self.size = size
        self.curr_size = 0
        self.list = LinkedList()
    
    def push(self,val):
        if self.curr_size < self.size :
            self.list.push(val)
        else:
            print("stack is full")
    
    def pop(self):
        if self.curr_size > 0:
            self.list.pop()
            self.curr_size -= 1
        else :
            print ("stack is empty")

    def peek(self, index) -> int:
        temp = self.list.head
        while index != 1 and temp:
            temp = temp.next
            index -= 1

        if temp is None:
            return -1
        else:
            return temp.val

    def top(self) -> int:
        return self.list.head.val
    
    def isEmpty(self) -> bool:
        if self.curr_size == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.curr_size == self.size:
            return True
        else:
            return False
    


st = Stack(5)
st.push(5)
st.peek(1)