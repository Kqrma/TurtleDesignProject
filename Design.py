import turtle
bob = turtle.Turtle()
from myFunction import*
turtle.colormode(255)
bob.speed(100)
turtle.bgcolor('black')


for times in range(100):
    bob.width(3)
    bob.color(times,0,times)
    polygonUnfill(bob,8,times)
    bob.right(100)
    bob.forward(10)
    
jump(bob,200,200)
for times in range (100):
    bob.width(5)
    bob.color(0,times,times)
    bob.circle(5-times)
    bob.right(135)

jump(bob,-200,200)
for times in range (100):
    bob.color(0,times,times)
    bob.circle(5-times)
    bob.right(135)

jump(bob,200,-200)
for times in range (100):
    bob.color(0,times,times)
    bob.circle(5-times)
    bob.right(135)

jump(bob,-200,-200)
for times in range (100):
    bob.color(0,times,times)
    bob.circle(5-times)
    bob.right(135)

jump(bob,0,0)
for times in range(100):
    bob.width(1)
    bob.color(times,times,times)
    bob.circle(times)
    bob.right(135)

    

