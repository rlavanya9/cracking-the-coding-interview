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

def calc(mystring):
    # 1 + 2 + 3*4
    # 1 * 2 * 8 + 10 - 27 * 2
    calc_stack = Stack()
    list_val = mystring.split()
    mult_operand = False
    div_operand = False
    add_sub = False
    value = None

    for element in list_val:
        if element in ['*','/','-','+']:
            if element == '*':
                mult_operand = True
            elif element == '/':
                div_operand = True
            elif element in ['-','+']:
                if value:
                    calc_stack.push(value)
                    value = None
                calc_stack.push(element)
                add_sub = True
        else:
            if mult_operand:
                value = value * int(element)
                mult_operand = False
            elif div_operand:
                value = value / int(element)
                div_operand = False
            elif add_sub:
                value = int(element)
                # calc_stack.push(element)
                add_sub = False
            else:
                value = int(element)
    if value:
        calc_stack.push(value)
    
    while len(calc_stack) != 0:
        node = calc_stack.pop()
        if node not in ['+','-','*','/']:
            input1 = int(node)  
        elif node == '+':
            calc_stack.push(int(calc_stack.pop()) + input1)
        elif node == '-':
            calc_stack.push(int(calc_stack.pop()) - input1)
        # elif node == '*':
        #     calc_stack.push(input1 * int(calc_stack.pop()))
    #     elif node == '/':
    #         calc_stack.push(input1 / int(calc_stack.pop()))
    return node

# print(calc("1 + 2 + 3 * 4"))  
# print(calc("1 + 2 "))     
print(calc("1 * 2 + 8 - 17"))
print(calc("1 * 2 * 8 + 10 - 27 * 2"))
print(calc("1 * 2 * 8 / 4 + 10 - 5 * 2"))