class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = 0
        self.right = 0

class Tree(object):
    def __init__(self,root):
        self.root = Node(root)
    
def is_BST(root,low = float('-inf'),high = float('inf')):
    if not root:
        return True
    
    val = root.data 
    if val <= low or val >= high:
        return False
    
    if not is_BST(root.left,low,val):
        return False
    if not is_BST(root.right,val,high):
        return False
    return True

root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (is_BST(root)): 
    print ("Is BST")
else: 
    print ("Not a BST")

root = Node(3)  
root.left = Node(2)  
root.right = Node(5)  
root.right.left = Node(1)  
root.right.right = Node(4)  
#root.right.left.left = Node(40) 
      
if (is_BST(root) == None): 
    print("Is BST") 
else: 
    print("Not a BST") 