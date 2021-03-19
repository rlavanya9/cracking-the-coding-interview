# class Stack(object):
#     def __init__(self):
#         self.items = []
    
#     def push(self,item):
#         self.items.append(item)
    
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
    
#     def is_empty(self):
#         return len(self.items) == 0
    
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
    
#     def size(self):
#         return len(self.items)
    
#     def __len(self):
#         return len(self.items)

class Q_stack():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self,item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return
        elif len(self.stack2)== 0 and len(self.stack1) > 0:
            while len(self.stack1):
                temp = self.stack1.pop()
                self.stack2.append(temp)
            return self.stack2.pop()
        else:
            return self.stack2.pop()

#         while len(self.stack1) > 0:
#             node1 = self.stack1.pop()
#             self.stack2.append(node1)
        
        
#         while len(self.stack2) > 0:
#             output = self.stack2.pop()
#         return output

# q = Q_stack() 
# q.enqueue(1) 
# q.enqueue(2) 
# q.enqueue(3) 

# print(q.dequeue()) 
# print(q.dequeue()) 
# print(q.dequeue()) class Queue: 
    # def __init__(self): 
    #     self.s1 = [] 
    #     self.s2 = [] 
  
    # # EnQueue item to the queue 
    # def enQueue(self, x): 
    #     self.s1.append(x) 
  
    # # DeQueue item from the queue 
    # def deQueue(self): 
  
    #     # if both the stacks are empty 
    #     if len(self.s1) == 0 and len(self.s2) == 0: 
    #         print("Q is Empty") 
    #         return
  
    #     # if s2 is empty and s1 has elements 
    #     elif len(self.s2) == 0 and len(self.s1) > 0: 
    #         while len(self.s1): 
    #             temp = self.s1.pop() 
    #             self.s2.append(temp) 
    #         return self.s2.pop() 
  
    #     else: 
    #         return self.s2.pop() 

q = Q_stack() 
q.enqueue(1) 
q.enqueue(2) 
q.enqueue(3) 

print(q.dequeue()) 
print(q.dequeue()) 
print(q.dequeue()) 