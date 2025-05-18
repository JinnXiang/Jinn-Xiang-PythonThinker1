# print("Hello from lesson 16")

import turtle

window = turtle.Screen()
window.setup(width=700, height=700)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("black")
t.pendown()


for i in range(500):
    t.forward(250)
    t.left(144)
    t.left(5)

window.mainloop()

def drawShape(length,num_sides):
    for i in range(num_sides):
        t.forward(length)
        t.right(360/num_sides)
draw