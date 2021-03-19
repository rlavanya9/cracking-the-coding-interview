class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = 0
        sel.right = 0

class Tree(object):
    def __init__(self,root):
        self.root = Node(root)

    def pre_order(self,start,traversal):
        def self.pre_order_helper(tree.root,"")

    def pre_order_helper(self,start,traversal):
        if start:
            traversal += str(start.data) + "-"
            traversal = pre_order(start.left, traversal)
            traversal = pre_order(start.right, traversal)
        return traversal

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)