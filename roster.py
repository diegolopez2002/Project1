class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, x):
        self.age = x
        

class Student(Person):
    
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def get_grade(self):
        return self.grade

    def change_grade(self, x):
        self.grade = x
        

class Staff(Person):

    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def get_position(self):
        return self.position

    def change_position(self, newPosition):

        self.position = newPosition
        return self.position


class Roster():

    def __init__(self):
        
        self.roster1 = []

    
    def add(self, Person): 
        self.roster1.append(Person)
        
    
    def size(self):
        return len(self.roster1)
        
        
    def remove(self, Person):
        self.roster1.remove(Person)
        

    def get_person(self, name):
        for Person in self.roster1:
            if Person.name == name:
                return Person
                
        return None
            
    def map(self, func):
        for Person in self.roster1:
            func(person)
            

        
