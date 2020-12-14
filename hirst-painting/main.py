import turtle as t
import random
#import colorgram
#
## Extract colors from an image.
#colors = colorgram.extract('image.jpeg', 30) 
#
#color_tuple = ()
#color_list = []
#num = 0
#for color in colors:
#    red = colors[num].rgb.r
#    green = colors[num].rgb.g
#    blue = colors[num].rgb.b
#    new_color = (red, green, blue)
#    num +=1
#    color_list.append(new_color)
#
#print(color_list)

color_list = [(34, 108, 142), (222, 155, 91), (9, 52, 86), (202, 133, 159), (35, 129, 75), (142, 78, 34),
              (22, 166, 200), (199, 156, 29), (138, 175, 195), (130, 30, 49), (204, 94, 122), (227, 210, 100),
              (149, 183, 164), (10, 98, 60), (10, 68, 127), (13, 45, 38), (215, 211, 16), (55, 53, 14),
              (169, 207, 181), (76, 77, 23), (179, 183, 215), (137, 65, 78), (9, 87, 109), (221, 102, 44),
              (87, 24, 42), (223, 174, 188)]

#Create Pen
pen = t.Turtle()
#Change color mode to numbered RGB
t.colormode(255)
#Lift up pen so that line is removed
pen.penup()
#Set starting co-ordinates for art piece
pen.setposition(-200, -200)
#Create a global 'Y Axis' variable to use after using inside make_row function
global y
y = -200
#Create a function to make a row of random colors
def make_row():
    """Makes a row of random color dots"""
    row = 0
    x = -200
    #Make a loop that will produce 10 dots
    while row < 10:
        #Set size and color of dot, make the dot color random
        pen.dot(20, color_list[random.randint(0, len(color_list) - 1)])
        #Position the dot
        pen.goto(x, y)
        #Increase dot movement by 50 and up the loop count by 1
        x += 50
        row += 1

#Create a loop that makes 10 colored rows
column = 0
while column < 10:
    make_row()
    y += 50
    column += 1






screen = t.Screen()
screen.exitonclick()
