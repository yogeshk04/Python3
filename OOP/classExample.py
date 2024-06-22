

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person('Yogesh', "Nikam", 31)
p2 = Person('Manu', "Nikam", 1)


print(p1.first_name,p1.last_name,p1.age)
