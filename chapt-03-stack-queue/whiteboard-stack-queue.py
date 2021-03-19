class Stack(object):
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def paran(mystring):
    stack = Stack()
    for element in mystring:
        if element in ['(','{','[']:
            stack.push(element)
        elif element == ')' and not stack.pop() == '(':
            return False
        elif element == '}' and not stack.pop() == '{':
            return False
        elif element == ']' and not stack.pop() == '[':
            return False
    return True
    # if stack.is_empty():
    #     return True
    # else:
    #     return False

# print(paran('(()())()'))
# print(paran('((())'))
# print(paran('())('))
# print(paran('{()}'))
# print(paran('[{)'))
                
                
# 123 -> [1, 2, 3]
# 6340 -> [6, 3, 4, 0]

class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.insert(0, item)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
# [1, 2, 3]
# [6, 3, 4, 0]
# [6, 4, 6, 3]
        
def sum_num(mylist1, mylist2):
    q = Queue()
    input1 = ""
    input2 = ""
    list_out = []
    for number in mylist1:
        q.enqueue(number)
    while not q.is_empty():
        input1 += str(q.dequeue())
    for number in mylist2:
        q.enqueue(number)
    while not q.is_empty():
        input2 += str(q.dequeue())
    
    output = int(input1) + int(input2)
    for number in str(output):
        list_out.append(number)
    return list_out

print(sum_num([1,2,3],[6,3,4,0]))
        
    
        
        