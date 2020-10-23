# methods inside class
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def newHi(self):
        print("Hi, My name is ", self.name)


o1 = Player("Developer", 45)
o1.age = 55

print(o1.age)
