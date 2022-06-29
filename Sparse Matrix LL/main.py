class Node:
    def __init__(self, column, value):
        self.column = column
        self.value = value
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def push(self, Newcolumn, Newvalue):
        newNode = Node(Newcolumn, Newvalue)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.column)
            print(temp.value)
            temp = temp.next


if __name__ == '__main__':

    sparseMatrix = []
    n = int(input("No. of rows:"))

    for i in range(n):
        llist = LinkList()
        m = int(input())
        column = list(map(int, input().split()))
        values = list(map(int, input().split()))
        for j in range(m, 0, -1):
            llist.push(column[j-1], values[j-1])
        sparseMatrix.append(llist)

    for i in range(len(sparseMatrix)):
        sparseMatrix[i].printList()
        print()
