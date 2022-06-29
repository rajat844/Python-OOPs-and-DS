class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


def nodeHeight(root):
    if not root:
        return 0
    return root.height


def balanceFactor(root):
    if not root:
        return 0
    return nodeHeight(root.left) - nodeHeight(root.right)


def LLRotation(p):
    pl = p.left
    plr = pl.right

    pl.right = p
    p.left = plr

    p.height = 1 + max(nodeHeight(p.left), nodeHeight(p.right))
    pl.height = 1 + max(nodeHeight(pl.left), nodeHeight(pl.right))

    return pl


def RRRotation(p):
    pr = p.right
    prl = pr.left

    pr.left = p
    p.right = prl

    p.height = 1 + max(nodeHeight(p.left), nodeHeight(p.right))
    pr.height = 1+max(nodeHeight(pr.left), nodeHeight(pr.right))

    return pr


def LRRotation(a):
    b = a.left
    c = b.right
    cl = c.left
    cr = c.right

    c.right = a
    c.left = b
    a.left = cr
    b.right = cl

    a.height = 1 + max(nodeHeight(a.left), nodeHeight(a.right))
    b.height = 1 + max(nodeHeight(b.left), nodeHeight(b.right))
    c.height = 1 + max(nodeHeight(c.left), nodeHeight(c.right))

    return c


def RLRotation(a):
    b = a.right
    c = b.left
    cl = c.left
    cr = c.right

    c.left = a
    c.right = b
    b.left = cr
    a.right = cl

    a.height = 1 + max(nodeHeight(a.left), nodeHeight(a.right))
    b.height = 1 + max(nodeHeight(b.left), nodeHeight(b.right))
    c.height = 1 + max(nodeHeight(c.left), nodeHeight(c.right))

    return c

def findlastright(parent):
    if not parent.right :
        return parent
    return findlastright(parent.right) 

def delhelper(parent):
    if not parent.left:
        return parent.right
    if not parent.right:
        return parent.left

    rightchild = parent.right
    lastright = findlastright(parent.left)
    lastright.right = rightchild

    return parent.left

def deleteNode(parent,key):
    if not parent :
        return parent
    
    if parent.val == key:
        return delhelper(parent)
    head = parent

    while head:
        if head.val > key:
            if not head.left and head.left.val == key:
                head.left = delhelper(head.left)
                break
            else :
                head = head.left
        
        if head.val < key :
            if not head.right and head.right.val == key:
                head.right = delhelper(head.right)
                break
            else :
                head = head.right

    
    
    return parent

def insertNode(parent, key):
    if parent == None:
        node = TreeNode(key)
        return node

    if (key < parent.val):
        parent.left = insertNode(parent.left, key)
    elif (key > parent.val):
        parent.right = insertNode(parent.right, key)

    parent.height = 1 + max(nodeHeight(parent.left), nodeHeight(parent.right))

    if balanceFactor(parent) == 2:
        if balanceFactor(parent.left) == 1:
            return LLRotation(parent)
        elif balanceFactor(parent.left) == -1:
            return LRRotation(parent)

    elif balanceFactor(parent) == -2:
        if balanceFactor(parent.right) == -1:
            return RRRotation(parent)
        elif balanceFactor(parent.right) == 1:
            return RLRotation(parent)

    return parent

def printTree(root):
    curr = root

    lst = []
    while curr:
        curr


