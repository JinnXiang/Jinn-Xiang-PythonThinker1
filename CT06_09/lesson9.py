print("Hello from lesson 9")

import random

num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)

print("1st number: " + str(num1))
print("2nd number: " + str(num2))
print("3rd number: " + str(num3))

num1_even = num1 % 2 == 0