# single array to three stacks
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

    def min(self):
        while not self.is_empty():
            val = self.peek()
            self.pop()

            if val < curr_min and curr_min != 0:
                curr_min = val
            elif curr_min == 0:
                curr_min = val
        return curr_min
                

    
def array_stack(myarr):
    stack1 = Stack()
    stack2 = Stack()
    stack3 = Stack()

    div_val = len(myarr)//3
    array1 = myarr[:div_val]
    array2 = 
    



    
