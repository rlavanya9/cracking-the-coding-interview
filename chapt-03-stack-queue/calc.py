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
    calc_stack = Stack()
    list_val = mystring.split()
    print(list_val)
    for element in list_val:
        if element == '+':
            calc_stack.push(calc_stack.pop() + calc_stack.pop())        
        elif element == '-':
            calc_stack.push(calc_stack.pop() - calc_stack.pop())
        elif element == '/':
            calc_stack.push(calc_stack.pop() / calc_stack.pop())
        elif element == '*':
            calc_stack.push(calc_stack.pop() * calc_stack.pop())
        else:
            calc_stack.push(int(element))
    return calc_stack.peek()


print(calc("1 2 + 3 4 * +"))
print(calc("124 4 * 57820 -"))