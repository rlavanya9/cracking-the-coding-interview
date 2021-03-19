class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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
    
    def __len__(self):
        return len(self.items)


def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.data)
        inorder(t.right)

def calc(mystring):
    operator = ['-','+','*','/']
    stack = Stack()
    for element in mystring:
        if element not in operator:
            t = Node(element)
            stack.push(t)
        else:
            t = Node(element)
            t1 = stack.pop()
            t2 = stack.pop()

            t.right = t1
            t.left = t2

            stack.push(t)
    t = stack.pop()
    return t

postfix = "12+45*6*-"
r = calc(postfix)
inorder(r)


        
# print(calc("1 * 2 + 8 - 17"))
# print(calc("1 * 2 * 8 + 10 - 27 * 2"))
# print(calc("1 * 2 * 8 / 4 + 10 - 5 * 2"))