import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("arrow")
tim.color("violet red")
tim.pensize(2)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color


#def  build_square(color):
#    tim.color(color)
#    for i in range(4):
#        tim.forward(100)
#        tim.right(90)
#
#build_square("dodger blue")
#build_square("lawn green")

#def dashed_line():
#    for i in range(10):
#        tim.forward(5)
#        tim.penup()
#        tim.forward(5)
#        tim.pendown()
#
#dashed_line()
#def shapes():
#    count = 3
#    while count < 11:
#        tim.color(random.choice(COLORS))
#        for i in range(count):
#            tim.forward(100)
#            tim.right(360/count)
#        count +=1
#shapes()    

#direction = [0, 90, 180, 270]
#count = 0
#while count < 250:
#    for i in range(count):
#        tim.color(random_color())
#        tim.forward(25)
#        tim.setheading(random.choice(direction))
#    count += 1      

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)










screen = t.Screen()
screen.exitonclick()
