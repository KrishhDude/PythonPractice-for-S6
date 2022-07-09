import turtle
t = turtle.Turtle()
n = int(input("Enter no. of sides"))
l = int(input("Enter length of each side"))
for i in range(n):
    t.forward(l)
    t.right(360/n)
