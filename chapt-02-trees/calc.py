# If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.

# If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.

# If the current token is a number, set the root value of the current node to the number and return to the parent.

# If the current token is a ')', go to the parent of the current node.


import operator
from pythonds.trees import BinaryTree
class node: 
    def __init__(self, value): 
        self.left = None
        self.data = value 
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

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()
# This function receives a node of the syntax tree 
# and recursively evaluate it 
# def evaluate(root): 
  
#     # empty tree 
#     if root is None: 
#         return 0
  
#     # leaf node 
#     if root.left is None and root.right is None: 
#         return int(root.data) 
  
#     # evaluate left tree 
#     left_sum = evaluateExpressionTree(root.left) 
  
#     # evaluate right tree 
#     right_sum = evaluateExpressionTree(root.right) 
  
#     # check which operation to apply 
#     if root.data == '+': 
#         return left_sum + right_sum 
      
#     elif root.data == '-': 
#         return left_sum - right_sum 
      
#     elif root.data == '*': 
#         return left_sum * right_sum 
      
#     else: 
#         return left_sum / right_sum 

pt = buildParseTree(" ( 10 + 5 ) * 3 ")
# pt = buildParseTree(" 1 + ( 2 * 3 ) + 4 ")
pt.postorder() 
# print(evaluate(pt))
