import platform
import random

new_rand = random.randint
print(new_rand(5, 200))


x = platform.system()
print(x)

y = dir(platform)
print(y)
