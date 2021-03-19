class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self,root):
        self.root = Node(root)

def sorted_array_tree(myarr):
    
    if not myarr:
        return None

    mid = len(myarr)// 2
    root = Node(myarr[mid])
    root.left = sorted_array_tree(myarr[:mid])
    root.right = sorted_array_tree(myarr[mid+1:])
    return root

def pre_order(start,traversal):
    return pre_order_helper(node.data,traversal)

def pre_order_helper(start,traversal):
    if start:
        traversal += str(start.data) + "_"
        traversal = pre_order(start.left,traversal)
        traversal = pre_order(start.right,traversal)
        return traversal


