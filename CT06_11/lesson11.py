# print("Hello from lesson 11")

px = int(input("What is the price of the item?"))
if px <= 5:
    print("Too cheap!")
elif px <= 50:
    print("Just spend more money.")
elif px <= 500:
    print("About right...Just a little more")
else:
    print("Yes! Perfect!")