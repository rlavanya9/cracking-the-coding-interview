class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = 0
        self.right = 0

class Tree(object):
    def __init__(self,root):
        self.root = Node(root)

def height_tree(root):
    if not root:
        return -1
    left_subtree = height_tree(root.left)
    right_subtree = height_tree(root.right)
    return 1 + max(left_subtree, right_subtree)

def is_balanced(root):
    if not root:
        return True
    ls = height_tree(root.left)
    rs = height_tree(root.right) 
    if is_balanced(root.left) and is_balanced(root.right) and abs(ls - rs) <= 1:
        return True

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.left.left.left = Node(8) 
if is_balanced(root): 
    print("Tree is balanced") 
else: 
    print("Tree is not balanced") 