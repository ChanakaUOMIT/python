# methods inside class
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def newHi(self):
        print("Hi, My name is ", self.name)


o1 = Player("Developer", 45)
print(o1)
# delete object
del o1
# print(o1)
