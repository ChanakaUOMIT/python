fruits = ["banana", "lemon", "apple", "orange"]

for i in fruits:
    print(i)

print("------------------")

for i in fruits:
    print(i)
    if i == "lemon":
        break

for i in fruits:
    print(i)
else:
    print("Completed Process!")

print("------------------")
for i in fruits:
    print(i)
    if i == "lemon":
        break
else:
    print("Completed Process!")
