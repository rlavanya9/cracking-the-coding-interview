class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = 0
        self.right = 0

class Tree(object):
    def __init__(self,root):
        self.root = Node(root)
# the left-most child in the right tree
def next_node(root,succ,key):
    if not root:
        return None
    
    if root.data == key:
        if root.right:
            root = root.right
            check_min(root)
    elif key < root.data:
        succ = root
        return next_node(root.left,succ,key)
    else:
        return next_node(root.right,succ,key)
    return succ



def check_min(root):
    while root.left:
        root = root.left
    return root
    
        

