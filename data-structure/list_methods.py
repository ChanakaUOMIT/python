# return number of items
cars = ["BMW", "Volvo", "Audi"]
print(len(cars))

# Access items
print(cars[0])
print(cars[1])
print(cars[0:2])
print(cars[-1])
print(cars[-2])
print(cars[-3])

fruits = ["banana", "lemon", "apple", "orange"]
fruits[1] = "change fruit"
print("Chnage ", fruits)

fruits.append("another fruits")
print("Append ", fruits)

del fruits[1]
print("Delete : ", fruits)
