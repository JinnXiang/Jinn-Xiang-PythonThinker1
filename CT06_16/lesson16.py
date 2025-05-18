# print("Hello from lesson 16")

import turtle

def setup_screen (screenWidth, screenHeight):
    screen = turtle.Screen()
    screen.setup(width = screenWidth, height = screenHeight)
    return screen

def create_blue_ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    return ball

screenWidth = 300
screenHeight = 500
screen = setup_screen(screenWidth, screenHeight)
ball = create_blue

screen.mainloop()


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