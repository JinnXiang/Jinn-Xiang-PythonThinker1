# print("Hello from lesson 13")

# account_balance = 1000
# withdraw = 0
# deposit = 0

# while True:

#     print("1. Withdraw")

#     print("2. Deposit")

#     print("3. Check Balance")

#     print("4. Exit")

#     User_Option = int(input("What do you choose to do?"))

#     if User_Option == 1:
#         withdraw = int(input("How much do you want to withdraw?"))
#         print("")
#         if account_balance < withdraw: 
#             print("Error, YOU ARE TRULY BROKE!!!")
#         else:
#             account_balance -= withdraw
#         print("Your current balance is:" + str(account_balance))

#     if User_Option == 2:
#         deposit = int(input("How much do you want to deposit?"))
#         print("")
#         account_balance += deposit
#         print("Your current balance is:" + str(account_balance))

#     if User_Option == 3:
#         print("Your current balance is:" + str(account_balance))
#         print("")

#     if User_Option == 4:
#         break

# groceries = [
#     "Apples",
#     "Bread"
#     "Carrots",
#     "Dates",
#     "Eggs",
#     "Flour",
#     "Grapes",
#     "Honey",
# ]
# groceries[6] = "Herbs"

# groceries.append("Ice")

# groceries.insert(1, "Bananas")

# del(groceries[2])

# print(groceries)

# for item in groceries:
#     if item == "Apples":
#         print(item + ": I need 5 of these")
#     elif item == "Carrots":
#         print(item + ": I need 3 of these")
#     elif item == "Grapes":
#         print(item + ": Get the NotFresh brand")
#     else:
#         print(item)

# pizza_toppings = [
#     "Mushrooms",
#     "Pepperoni",
#     "Pineapple",
#     "Bacon",
#     "Chicken",
#     "Beef",
#     "Sauce"
# ]
# user_toppings = []
# print("Your available toppings: ")
# for i in range (len(pizza_toppings)):
#     print(str(i + 1) + ". " + pizza_toppings[i])
# while True:
#     choice = input("What toppings do you want? Give me the number: ")
#     if choice == "end":
#         break
#     else:
#         user_toppings.append(pizza_toppings[int(choice) - 1])
# for item in user_toppings:
#     print(item)