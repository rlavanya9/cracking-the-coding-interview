from dataclasses import dataclass  # if python < 3.7
from typing import Optional, List
from operator import add, sub, mul, truediv

class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)
    
    def size(self):
        return len(self.items)
        
@dataclass
class Node:
    symbol: str
    left: Optional['Node']
    right: Optional['Node']

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

@dataclass
class Tree:
    root: Node
    # negative numbers, numbers with space
    @classmethod
    def _tokenize(cls, text: str) -> List[str]: 
        prev = ''
        tokenized = []
        for char in text:
            if prev.isdigit() and char.isdigit():
                tokenized.append(tokenized.pop() + char)
            else:
                tokenized.append(char)
            prev = char
        return tokenized

    @classmethod
    def build(cls, text: str) -> 'Tree':
        operator_stack: List[str] = []
        operand_stack: List[Node] = []
        for char in cls._tokenize(text):
            # print(operator_stack, operand_stack)
            if char.isdigit():
                operand_stack.append(Node(symbol=char, left=None, right=None))
            elif char in '+-' and len(operator_stack) > 0 and operator_stack[-1] in '*/':
                right = operand_stack.pop()
                op = operator_stack.pop()
                left = operand_stack.pop()
                operand_stack.append(Node(symbol=op, left=left, right=right))
                operator_stack.append(char)
            elif char == ')':
                while len(operator_stack) > 0 and operator_stack[-1] != '(':
                    right = operand_stack.pop()
                    op = operator_stack.pop()
                    left = operand_stack.pop()
                    operand_stack.append(Node(symbol=op, left=left, right=right))
                operator_stack.pop()
            else:
                operator_stack.append(char)
        while len(operator_stack) > 0:
            right = operand_stack.pop()
            op = operator_stack.pop()
            left = operand_stack.pop()
            operand_stack.append(Node(symbol=op, left=left, right=right))
        return cls(root=operand_stack.pop())

    def evaluate(self, node: Optional[Node] = None):
        OPS = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': truediv
        }
        node = node or self.root
        if node.is_leaf():
            return int(node.symbol)
        else:
            op = OPS[node.symbol]
            return op(self.evaluate(node.left), self.evaluate(node.right))

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

# tree = Tree.build('(2+3)*2+7*3')
tree = Tree.build('1+(2*3)+4')  
print(pre_traverse_help(tree.root))
# print(tree.evaluate())