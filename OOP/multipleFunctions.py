class DoMath:

    def addition(self, x, y):
        return x+y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x*y


# first object
first_object = DoMath()
print(first_object.addition(5, 6))
print(first_object.subtraction(7, 8))
print(first_object.multiplication(10, 11))

# second object
second_object = DoMath()
print(second_object.addition(21, 22))
print(second_object.subtraction(25, 20))
print(second_object.multiplication(5, 8))
