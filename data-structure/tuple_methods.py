# list inside tuple
mixed = ("Apple", [10, 20, 30])
print(mixed)

# access item
fruits = ("apple", "orange", "lemon", "fig")
print(fruits[2])
print(fruits[0:3])

# update tuple items
fruits = ("orange", "lemon", "banana")
print(fruits)

# reassign items
fruits = ("apple", "fig")
print(fruits)


# tuple concatenation
fruits1 = ("orange", "lemon", "banana")
fruits2 = ("apple", "fig")
allFruits = fruits1 + fruits2
print(allFruits)

# delete tuple
del fruits1
# print(fruits1)
