
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        print(self.name, "can drive")

class Child(Adult):
    def __init__(self, name, age, hair_colour, eye_colour):
        super().__init__(name, age, hair_colour, eye_colour)

    def can_drive(self):
        print(self.name, "is too young to drive")


name = input("Input person's name: ")
age = int(input("Please input person's age: "))
hair_colour = input("Please input person's hair colour: ")
eye_colour = input("Please input person's eye colour: ")

if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)

person.can_drive()