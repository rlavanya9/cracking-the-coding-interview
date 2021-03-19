class Node(self,data):
    self.data = data
    self.left = None
    self.right = None

def form_tree(mystr):
    for element in mystr:
        # find the least order precedence
        operand_stack = Stack()
        operator_stack = Stack()
        if element.isdigit():
            operand_stack.push(element)
        elif element in '+-' and len(operator_stack) > 0 and operator_stack[-1] in '*/':
            right = operand_stack.pop()
            op = operator_stack.pop()
            left = opeand_stack.pop()
            

