# print("Hello from lesson 11")

px = int(input("What is the price of the item?"))
if px <= 5:
    print("Too cheap!")
elif px <= 50:
    print("Are you sure you need this?")
elif px <= 500:
    print("Where are you getting this money from?!")
else:
    print("Don't even think about it!")