class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly Linked List
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        curr = self.head
        count = 0

        while curr != None:
            count += 1
            curr = curr.next_node
        return count

    def search(self, key):
        curr = self.head

        while curr:
            if curr.data == key:
                return curr
            else:
                curr = curr.next_node
            return print("no such node exist")

    def add(self, data):
        '''
        Adds new node to head of the data
        Time O(n)
        '''
        if self.is_empty() == True:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

        else:
            new_node = Node(data)
            self.tail.next_node = new_node
            self.tail = new_node

    def insert(self, data, index):
        if index == 0:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node
        else:
            new_node = Node(data)

            position = index
            curr = self.head

            while(curr and position > 1):
                curr = curr.next_node
                position -= 1

            if position > 0:
                return False
            else:
                a = curr.next_node
                curr.next_node = new_node
                new_node.next_node = a
