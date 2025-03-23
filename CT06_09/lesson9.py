print("Hello from lesson 9")

import random

num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)

print("1st number: " + str(num1))
print("2nd number: " + str(num2))
print("3rd number: " + str(num3))

num1_even = num1 % 2 == 0
num2_even = num2 % 2 == 0
num3_even = num3 % 2 == 0

all_even_odd = num1_even == num2_even == num3_even
print("All numbers are even")