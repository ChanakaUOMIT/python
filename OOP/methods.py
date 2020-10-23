# methods inside class
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def newHi(self):
        print("Hi, My name is ", self.name)


o1 = Player("Developer", 45)
del o1.age
print(o1.name)
# print(o1.age)
o1.newHi()
