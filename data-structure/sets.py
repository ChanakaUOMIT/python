newFruits = {"Fig", "Lemon", "Cherry"}
print(newFruits)

for x in newFruits:
    print(x)

print("banana" in newFruits)
print("Fig" in newFruits)


newFruits.add("orange")
print(newFruits)

newFruits.update(["Mango", "Grapes"])
print(newFruits)

print(len(newFruits))

newFruits.remove("Fig")
print(newFruits)

x = newFruits.pop()
print(x)
print(newFruits)

newFruits.clear()
print(newFruits)

del newFruits
# print(newFruits)
