# 1 Basic subclasses - Adam and Eve

class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    Adam = Man()
    Eva = Woman()
    return [Adam, Eva]

print(God())

print('---'*100)

# 2 OOP: Object Oriented Piracy

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        if self.draft - (1.5 * self.crew) > 20:
            return True
        else:
            return False

Titanic = Ship(0, 0)
Titanic.is_worth_it()

print('---'*100)

# 3 Classic Hello World

class Solution():
    def main(*args):
        print("Hello World!")

Solution.main("parameter1", "parameter2", "parametern")