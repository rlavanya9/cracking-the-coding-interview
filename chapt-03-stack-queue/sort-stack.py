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
    
    def prints(self):
        for i in range(len(self.items)):
            print(self.items[i])
        # while not self.is_empty():
        #     val = self.peek()
        #     print(val)
        #     self.pop()
        # for i in range(len(stk)-1, -1, -1): 
        #     print(stk[i], end = ' ') 
        # print() 
        

def Sorted_stack(inp_stack):
        # inp_stack = Stack()
        tmp_stack = Stack()
        while not inp_stack.is_empty():    
            tmp_value = tmp_stack.peek()
            item = inp_stack.peek()
            item = inp_stack.pop()
            while not tmp_stack.is_empty() and tmp_value > item:
                node = tmp_stack.peek()
                inp_stack.push(node)
                tmp_stack.pop()
                    
            tmp_stack.push(item)
        return tmp_stack

stack = Stack()
stack.push(str(34))
stack.push(str(3))
stack.push(str(31)) 
stack.push(str(98)) 
stack.push(str(92)) 
stack.push(str(23))
sortedst = Sorted_stack(stack) 
sortedst.prints() 