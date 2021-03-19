class Node(object):
    def __init__(self,data,next):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class LinkedList(object):
    def __init__(self,head):
        self.head = head
    
    def insert(self,node):
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def pop_head(self):
        if self.head is None:
            return None
        pop_val = self.head
        self.head = self.head.next
        return pop_val
    
    def size(self):
        current = self.head
        while current.next is not None:
            size += 1
            current = current.next
        return size

class Animal(object):
    def __init__(self,name,time):
        self.name = name
        self.time = time.time()

class Cat(object):
    pass

class Dog(object):
    pass

class AnimalShelter(LinkedList):
    def enqueue(self,animal):
        animal_node = Node(animal)
        self.insert(animal_node)
    
    def dequeue(self):
        return super().pop_head()

    def dequeue_cat(self):
        prev = None
        current = self.head
        while current.next is not None:
            if isinstance(current.data, Cat):
                prev.next = current.next
                return current.data
            prev = current
            current = current.next
        return None

    def dequeue_dog(self):
        prev = None
        current = self.head
        while current.next is not None:
            if isinstance(current.data, Dog):
                prev.next = current.next
                return current.data
            prev = current
            current = current.next
        return None

def test_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("Fluffy"))
    animal_shelter.enqueue(Dog("Sparky"))
    animal_shelter.enqueue(Cat("Sneezy"))
    assert animal_shelter.size() == 3