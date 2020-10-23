# anonymouse with one arg
def new_multiplied(k):
    print("k : ", k)
    return lambda x: x*k


new_double = new_multiplied(2)  # k=2
new_triple = new_multiplied(3)  # k=3

print(new_double(12))  # x =12
print(new_triple(12))  # x=12
