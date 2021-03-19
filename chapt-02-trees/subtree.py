class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = 0
        self.right = 0

class Tree(object):
    def __init__(self,root):
        self.root = Node(root)

def subtree(t1, t2):
    if not t1.root:
        return None
    
    if t1.root == t2.root:

        while t1.root.left:
            if t1.root.left != t2.root.left:
                return False

        while t2.root.right:
            if t1.root.right != t2.root.right:
                return False
        
        return True

    else:
        if t1.root < t2.root:
            subtree(t1.root.left, t2.root.left)
        else:
            subtree(t2.root.right,t2.root.left)    

T = Node(26) 
T.right = Node(3) 
T.right.right  = Node(3) 
T.left = Node(10) 
T.left.left = Node(4) 
T.left.left.right = Node(30) 
T.left.right = Node(6) 

S = Node(10) 
S.right = Node(6) 
S.left = Node(4) 
S.left.right = Node(30) 

if subtree(T, S): 
    print ("Tree 2 is subtree of Tree 1")
else : 
    print ("Tree 2 is not a subtree of Tree 1")