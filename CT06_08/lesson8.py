# print("Hello from lesson 8")

# for h in range(5):
#     num=input("Tell me a number")
# print(int(num)*5)

result = 1

# Use a for loop to ask for 5 numbers
for i in range(5):
    num = float(input("Enter number {}: ".format(i+1)))  # Input for each number
    result *= num  # Multiply the result by the entered number

# Print the final multiplication result
print("The multiplication of the entered numbers is: {}".format(result))