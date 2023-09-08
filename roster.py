#Diego Lopez roster


class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def get_age(self):

        return self.age


    def set_age(self, x):

        int(self.age)
        self.age = x
        return self
    

class Student(Person):

    def __init__(self, name, age, grade):
        
        super().__init__(name,age)
        self.grade = grade


    def get_grade(self):
        return self.grade
        

    def change_grade(self, x):
        self.grade = x
        return self


class Staff(Person):

    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position


    def get_position(self):
        
        return self.position

    def change_position(self, newPosition):

        self.position = newPosition
        return self.position


class Roster:

    size = 0

    def __init__(self):

        self.persons = []
        
    def add(self, person):
        
        self.persons.append(person)
            
            
    def size(size):
        return size
        
    def remove(self, Person):

        self.persons.remove(Person)
        size -= 1


    def get_person(self, name):

        if name not in self.persons:
            return None
        
        self.name = name
        return name

        
    def map():

        pass



