class Stack(object):
    def __init__(self,capacity):
        self.stacks = []
        if capacity > 1:
            self.capacity = capacity

    def push(self,item):
        if len(self.stacks) == 0:
            self.stacks.append([item])
    
        if self.stacks[-1] >= self.capacity:
            self.stacks[-1].append([item])
        else:
            self.stacks[-1].append(item)

    def pop(self):
        if not self.stacks:
            return "No item to return;stack is empty"
        else:
            popped_data = self.stacks[-1][-1]

            if len(self.stacks[-1]) == 1:
                del self.stacks[-1]
            else:
                del self.stacks[-1][-1]
            return popped_data

    def pop_at_index(self,index):
        if self.stacks == []:
            return "stack is empty"
        elif index-1 > len(self.stacks):
            return "index out of range"
        else:
            if len(self.stacks) == index:
                del self.stacks[-1][-1]
            else:
                self.stacks[index-1][-1] = self.stacks[index][0]
                for i in range(index, len(self.stacks)):
                    for j in range(0, len(self.stacks[i])-1):
                        self.stacks[i][j] = self.stacks[i][j+1]
                    if i < len(self.stacks)-1:
                        self.stacks[i][-1] = self.stacks[i+1][0]
                    del self.stacks[-1][-1]

                    if len(self.stacks[-1]) == 0:
                        del self.stacks[-1]
        