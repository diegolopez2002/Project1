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


class roster():


    def __init__(self):
        
        self.persons = []
        
        
    def add(self, person):
        
        self.persons.append(person)
        
        
        
    def size(self):
        
        return len(self.persons)
        
        
    def remove(self, person):

        if person in self.persons:
            self.persons.remove(Person)
        


    def get_person(self, name):

        for self.person in persons:
            if self.person.name == name:
                return self.person

        return None
            

        
    def map(self):
        pass

        
        
        
        



