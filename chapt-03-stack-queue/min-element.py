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

class Min_Stack(object):
    def __init__(self):
        stack = Stack()
        self.min_val = None
    
    def push_min(self, item):
        if not stack:
            stack.push(item)
            self.min_val = item
        
        elif item < self.min_val:
            stack.push(2*item - self.min_val)            
            self.min_val = item

        else:
            stack.push(item)
    
    def pop_min(self):
        top = stack.peek()
        if top < self.min_val:
            self.min_val = (2*self.min_val - top)
        stack.pop() 
    
    def min_val_ret(self):
        return self.min_val