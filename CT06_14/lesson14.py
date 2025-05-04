# print("Hello from lesson 14")
import turtle
window = turtle.Screen()
window.setup(width=700, height=700)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("black")
t.seth(0)
t.pendown()
for i in range(500):
    t.forward(250)
    t.left(144)
window.mainloop()