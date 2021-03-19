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

class Tower(object):
    def __init__(self, number, start, final, middle):
        self.number = number
        self.towers = {
            start : Stack(),
            final : Stack(),
            middle : Stack()
        }
        for i in range(number,0,-1):
            self.towers[start].push(i)
    
    def tower_print(self,start,final):
        self.towers[final].push(self.towers[start].pop())
        print(f"move from {start} to {final}")

    def tower_recur(self, number, start, final, middle):
        if number >= 1:
            self.tower_recur(number-1,start,middle,final)
            self.tower_print(start,final)
            self.tower_recur(number-1,middle,final,start)

tower = Tower(3,'A','B','C')
tower.tower_recur(3,'A','B','C')
