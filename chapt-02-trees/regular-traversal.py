class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = 0
        self.right = 0

class Tree(object):
    def __init__(self,root):
        self.root = Node(root)

# def pre_traverse(start,traversal):
#     return pre_traverse_help(tree.root, "")
class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __len(self):
        return len(self.items)

def pre_traverse_help(root):
    if root is None:
        return None

    stack = Stack()
    stack.push(root)

    while stack:
        curr = stack.pop()
        print(curr.data)

        if curr.right:
            stack.push(curr.right)
        
        if curr.left:
            stack.push(curr.left)
        
        
    
def in_order(root):

    if root is None:
        return None

    curr = root
    stack = Stack()
    while stack or curr:
        if curr:
            stack.push(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data)
            curr = curr.right


def post_order(root):
    stack = Stack()
    out = Stack()

    stack.push(root)
    while stack:
        curr = stack.pop()
        out.push(curr.data)

        if curr.left:
            stack.push(curr.left)
        if curr.right:
            stack.push(curr.right)
    
    while out:
        print(out.pop())


       

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
print(pre_traverse_help(tree.root,""))
    
