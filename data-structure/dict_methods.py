# create a fruit price dict
fruit_price = {"Apple": 5, "Banana": 4, "Fig": 3, "Grap": [5, 6, 7]}
print(fruit_price["Apple"])  # 5
print(fruit_price.get("Banana"))  # 4
print(fruit_price.get("Orange"))  # None
print(fruit_price["Grap"][1])  # 6


player_number = {"Messi": 10, "Ronaldo": 7, "Salah": 11}

# update Ronaldo numbers
player_number["Ronaldo"] = 17
print(player_number)

# add item
player_number["Pogba"] = 6
print(player_number)

# delete item
del player_number["Ronaldo"]
print(player_number)

del player_number
# print(player_number)
