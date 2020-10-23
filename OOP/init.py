# using __init__ method
class NewClass:

    def __init__(self):
        self.a = "Hello"

    def hi(self):
        return "hi there!"


# first object
first_object = NewClass()


# display the result
print(first_object.a)
print(first_object.hi())
