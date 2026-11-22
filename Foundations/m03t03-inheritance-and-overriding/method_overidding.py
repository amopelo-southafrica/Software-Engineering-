name = input("Whats is your name?")
age = int(input("Whats is your age?"))
eye_color = input("Whats is your eye color?")
hair_color = input("Whats is your hair color?")

class Adult:
    def __init__(self,name,age,eye_color,hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color
        pass
    def can_drive(self):
        print(f"{self.name}, you are old enough to drive")

class Child(Adult):
    def can_drive(self):
        print(f"{self.name}, you are too young to drive")

adult_1 = Adult(name,age,eye_color,hair_color)
child_1 = Child(name,age,eye_color,hair_color)

if age >= 18:
    print(adult_1.can_drive())
else:
    print(child_1.can_drive())

   

