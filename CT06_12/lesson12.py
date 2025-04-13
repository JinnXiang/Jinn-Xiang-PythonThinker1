# print("Hello from lesson 12")

# num=int(input("What is the number?"))
# if num % 3 == 0 and num % 5 == 0:
#     print("Divisible by 3 and 5")
# else:
#     print("Not divisible by 3 and 5")

# vis = 0
# while vis < 50:
#     vis += 1
#     print(vis)

# vis = 18
# while vis < 30:
#     vis += 1
#     print(vis)

# vis = 4
# while vis < 25:
#     vis += 1
#     print(vis)

# max = 30
# vis = 0

# while True:
#     userinput = input("Add visitor?")
#     if userinput == "yes":
#         vis += 1
#         print(vis)
#     if vis == max:
#         break
# print("Full")

# order = ""
# Skipcomma = True
# while True:
#      item = input("What is your order?")
#      if item == "nothing else":
#          break
#      else:
#         if Skipcomma:
#             order += item
#             Skipcomma = False
#         else:
#             order = order + ", " + item

num = 10
while num != 0:
    print(num)
    num -= 1
else:
    print