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

class AnimalShelter(object):
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0
    
    def add_animal(self,name,kind):
        kind = kind.lower()
        self.order += 1
        animal = {
            "name" : name,
            "type" : kind,
            "order" : self.order           
        }
        if kind == "cat":
            self.cats.append(animal)
        elif kind == "dog":
            self.dogs.append(animal)
        else:
            print("Invalid Input")
    
    def adopt_animal(self,animal_list):
        if len(animal_list) == 0:
            return None
        return animal_list.pop(0)
    
    def adopt_cat(self):
        return self.adopt_animal(self.cats)
    
    def adopt_dog(self):
        return self.adopt_animal(self.dogs)
    
    def adopt_any(self):
        if len(self.cats)==0:
            return self.adopt_dog()
        elif len(self.dogs) > 0 and self.cats[0]["order"] > self.dogs[0]["order"]:
            return self.adopt_dog()
        else:
            return self.adopt_cat()

a = AnimalShelter()
a.add_animal("Pizzapie", "cat")
a.add_animal("Emmy", "Dog")
a.add_animal("Sushi", "Cat")
a.add_animal("Charmander", "Dog")
print(a.cats, a.dogs)

a.adopt_cat()
a.adopt_dog()
a.adopt_any()
print(a.cats, a.dogs)
        
