#Diego Lopez roster


class Person:

    def __init__(self,name,age):

        self.name = name
        self.age = age


    def getAge(self):
    
        return self.age


    def setAge(x, self):

        self.age = x
        return x
    

class Student:

    def __init__(self,name,age, grade):

        self.grade = grade
        return super().__init__(name,age,grade)


    def get_grade(self):

        return self.grade
        

    def change_grade(x,self):

        self.grade = x
        return self.grade



class Staff:


    def __init__(self, name, age, position):
        
        self.position = position
        return super().__init__(name,age,position)


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

        if isinstance(person, Person) or isinstance(person, Staff) or isinstance(person, Student):
            self.persons.append(person)
            size += 1
            
            
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



