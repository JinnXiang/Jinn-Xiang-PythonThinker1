# print("Hello from lesson 16")

# import turtle

# def setup_screen (screenWidth, screenHeight):
#     screen = turtle.Screen()
#     screen.setup(width = screenWidth, height = screenHeight)
#     return screen

# def create_blue_ball():
#     ball = turtle.Turtle()
#     ball.shape("circle")
#     ball.color("blue")
#     ball.penup()
#     return ball

# def move_ball(ball, dx, dy):
#     ball.setx(ball.xcor() + dx)
#     ball.sety(ball.ycor() + dy)

# def check_x(ball, screenWidth):
#     if ball.xcor() > (screenWidth / 2) or ball.xcor() < (-screenWidth / 2):
#         return True

# def check_y(ball, screenHeight):
#     if ball.ycor() > (screenHeight / 2) or ball.ycor() < (-screenHeight / 2):
#         return True


# screenWidth = 300
# screenHeight = 500
# screen = setup_screen(screenWidth, screenHeight)
# ball = create_blue_ball()

# dx = 2
# dy = 2
# while True:
#     move_ball(ball, dx, dy)
#     if check_x(ball, screenWidth):
#         dx *= -1
#     if check_y(ball, screenHeight):
#         dy *= -1

# screen.mainloop()




# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("black")
# t.pendown()






# for i in range(500):
#     t.forward(250)
#     t.left(300)
#     t.left(5)


# def drawShape(length,num_sides):
#     for i in range(num_sides):
#         t.forward(length)
#         t.right(360/num_sides)
# drawShape(100,50)
# window.mainloop()