# Murtajiz Mehdi
# Begin date: October 27th, 2022

# Create a program that asks a series of questions in order to determine what hero the user matches the best with.
# This program will be using turtles library in order to draw out the logo of given hero.


# CODE BEGINS HERE -----------------------------------------------------------------------------------------------------

# import turtle library in order to create graphic designs. Many designs will be pre-made with credit to original source
import turtle, math


# ALL HERO LOGOS ---------------------

# superMan logo - Try to create a Sharper design
def superManLogo():
    t = turtle.Turtle()  # set the variable ‘t’ to the function turtle.Turtle() to shorten the code throughout
    turtle.Screen().bgcolor('navy')  # set the color of the screen to navy to match Superman’s costume
    turtle.title("YOU ARE SUPERMAN")

    def curve(value):  # create a function to generate curves in turtle
        for i in range(value):  # for loop to repeat the inputted value number of times
            t.right(1)  # step by step curve
            t.forward(1)

    t.penup()  # pen is in the up position so it will not draw
    t.setposition(0, 43)  # move the pen to these x and y coordinates
    t.pendown()  # pen is in the down position so it will draw
    t.begin_fill()  # start filling in the shape
    t.pencolor('black')  # change the pen color to black
    t.fillcolor('maroon')  # change the shape fill color to maroon to match the Superman logo
    t.pensize(3)  # use a pen size of 3 to create a black border
    t.forward(81.5)  # the pen will move forward this number to start the shield of the logo
    t.right(49.4)  # rotate the pen right 49.4 degrees
    t.forward(58)  # move the pen forward by 58
    t.right(81.42)  # rotate right by 81.42 degrees
    t.forward(182)  # move the pen forward by 182
    t.right(98.36)  # rotate the pen right by 98.36 degrees
    t.forward(182)  # move the pen forward by 182
    t.right(81.42)  # rotate the pen by 81.42 degrees to the right
    t.forward(58)  # move the pen forward 58
    t.right(49.4)  # rotate the pen to the right by 49.4
    t.forward(81.5)  # move the pen forward by 81.5 to meet the start at the top of the shield
    t.end_fill()  # complete the fill of the shield so the shape is closed off
    t.penup()  # pen will not draw

    t.setposition(38, 32)  # now to create the yellow parts of the Superman logo
    t.pendown()  # the pen is now poised to draw
    t.begin_fill()  # start a new shape
    t.fillcolor('gold')  # change the fill color to gold to match the Superman logo
    t.forward(13)  # move the pen forward by 13
    t.right(120)  # rotate the pen right by 120 degrees
    t.forward(13)  # move the pen forward by 13
    t.right(120)  # rotate the pen right by 120 degrees
    t.forward(13)  # move the pen forward by 13
    t.end_fill()  # the small triangle on the right is now complete
    t.penup()  # stop the pen from drawing

    t.setposition(81.5, 25)  # now to create the larger yellow part of the Superman logo, change the position of the pen
    t.pendown()  # the pen will now draw again
    t.begin_fill()  # the fill is still the same color set before
    t.right(210)  # rotate the pen right by 210 degrees
    t.forward(25)  # move the pen forward by 25
    t.right(90)  # rotate the pen right by 90 degrees
    t.forward(38)  # move the pen forward by 38
    t.right(45)  # rotate the pen right by 45 degrees
    t.circle(82,
             90)  # this function is used to draw a circle in turtle, the first integer is the radius and the second is the number of degrees of the circle drawn
    t.left(90)  # rotate the pen left by 90 degrees
    t.circle(82, 60)  # create a circle of radius 82 and only complete 60 degrees of the circle
    curve(
        61)  # call the curve function that was previously defined, pass an integer value equal to the length of the curve desired
    t.left(90)  # rotate the pen left by 90 degrees
    t.forward(57)  # move the pen forward by 57
    t.left(90)  # rotate the pen left by 90 degrees
    t.forward(32)  # move the pen forward by 32
    t.end_fill()  # fill in the larger yellow part of the logo
    t.penup()  # stop drawing
    t.home()  # reset the pen location to the origin so the orientation is also reset

    t.setposition(-69, -38)  # finish the major parts of the S superimposition on the shield
    t.pendown()
    t.begin_fill()
    curve(20)
    t.forward(33)
    t.left(10)
    t.circle(82, 20)
    curve(30)
    t.forward(10)
    t.right(110)
    curve(40)
    t.right(10)
    t.circle(50, 10)
    curve(45)
    t.right(5)
    t.forward(45)
    t.end_fill()
    t.penup()
    t.home()

    t.setposition(20, -100)
    t.pendown()
    t.begin_fill()
    t.right(135)
    t.forward(27)
    t.right(90)
    t.forward(27)
    t.right(135)
    t.forward(38.18)
    t.end_fill()
    t.penup()
    t.home()

    t.setposition(-57, 32)
    t.pendown()
    t.begin_fill()
    t.right(180)
    t.forward(18)
    t.left(45)
    t.forward(44)
    t.left(80)
    t.forward(15)
    t.left(130)
    curve(40)
    t.forward(20)
    t.end_fill()

    t.hideturtle()
    turtle.exitonclick()

    # Code cited from Harry from CopyAssignment.com

# spiderMan logo - Refactor in order to make code run faster
def spiderManLogo():
    import turtle
    turtle.title("YOU ARE SPIDER-MAN")
    turtle.bgcolor('black')
    p = turtle.Turtle()
    wn = turtle.Screen()
    p.pencolor('red')
    p.hideturtle()

    # curve01
    def curve01(a, d):
        for i in range(d):
            p.right(a)
            p.forward(1)

    # making eye
    p.width(15)
    p.penup()
    p.right(90)
    p.forward(85)
    p.left(90)
    p.forward(35)
    p.pendown()
    p.fillcolor('white')
    p.begin_fill()
    p.left(55)
    curve01(0.09, 100)
    curve01(0.2, 100)
    p.forward(70)
    p.right(90)
    curve01(0.5, 100)
    curve01(00, 30)
    curve01(0.3, 50)
    curve01(0.6, 50)
    p.forward(50)
    p.right(47)
    curve01(0.1, 95)
    p.end_fill()

    # changing
    p.penup()
    p.left(36)
    p.forward(70)
    p.pendown()

    # curve02
    def curve02(a, d):
        for i in range(d):
            p.left(a)
            p.forward(1)

    # second eye
    p.fillcolor('white')
    p.begin_fill()
    p.right(55)
    curve02(0.09, 100)
    curve02(0.2, 100)
    p.forward(70)
    p.left(90)
    curve02(0.5, 100)
    curve02(00, 30)
    curve02(0.3, 50)
    curve02(0.6, 50)
    p.forward(50)
    p.left(47)
    curve02(0.1, 95)
    p.end_fill()

    p.penup()
    p.width(0)
    p.right(49)
    p.forward(30)
    p.left(102)  # 100.40
    p.forward(145)
    p.pencolor('red')

    # making left face
    p.fillcolor('red')
    p.begin_fill()
    p.speed(0)
    p.pendown()
    p.left(90)
    curve01(5, 20)
    p.left(175)
    p.forward(50)
    p.left(25)
    p.forward(28)
    p.right(160)
    p.forward(170)
    curve02(0.2, 65)
    p.right(60)
    curve01(0.1, 140)
    curve01(0.5, 50)
    p.left(180)
    curve02(0.2, 150)
    curve02(0.1, 95)
    p.left(127)
    p.forward(5)
    curve01(2, 20)
    p.right(30)
    p.forward(90)
    p.right(7)
    p.forward(75)
    p.right(160)
    p.forward(100)
    curve02(0.1, 105)
    p.right(70)
    curve01(0.2, 200)
    curve01(0.3, 70)
    p.left(175)
    curve02(0.2, 150)
    curve02(0.3, 150)
    p.forward(20)
    p.left(65)
    curve01(0.1, 120)
    curve01(0.010, 105)
    p.right(10)
    curve01(0.2, 110)
    p.right(60)
    curve01(0.3, 138)
    p.right(30)
    curve01(0.2, 160)
    p.left(150)
    curve02(0.2, 100)
    curve02(0.1, 150)
    p.forward(70)
    curve02(0.4, 40)
    p.left(160)
    curve01(0.1, 60)
    p.left(7)
    curve01(0.1, 120)
    curve01(0.2, 30)
    p.forward(20)
    p.right(140)
    curve02(0.2, 40)
    p.right(50)
    curve02(0.2, 70)
    p.right(8)
    curve02(0.1, 70)
    curve02(0.5, 50)
    p.left(153)
    curve01(0.1, 170)
    p.right(81)
    curve02(0.2, 20)
    p.right(3)
    curve02(0.1, 62)
    p.right(153)  # ..
    curve01(0.1, 63)
    p.left(50)
    curve02(0.1, 175)
    p.left(60)
    p.forward(7)
    p.end_fill()

    # going to replicate
    p.left(92.15)
    p.penup()
    p.forward(417)
    p.pendown()

    p.fillcolor('red')
    p.begin_fill()
    # right face
    p.right(90)
    curve02(5, 20)
    p.right(175)
    p.forward(50)
    p.right(25)
    p.forward(28)
    p.left(160)
    p.forward(170)
    curve01(0.2, 65)
    p.left(60)
    curve02(0.1, 140)
    curve02(0.5, 50)
    p.right(180)
    curve01(0.2, 150)
    curve01(0.1, 95)
    p.right(127)
    p.forward(5)
    curve02(2, 20)
    p.left(30)
    p.forward(90)
    p.left(7)
    p.forward(75)
    p.left(160)
    p.forward(100)
    curve01(0.1, 105)
    p.left(70)
    curve02(0.2, 200)
    curve02(0.3, 70)
    p.right(175)
    curve01(0.2, 150)
    curve01(0.3, 150)
    p.forward(20)
    p.right(65)
    curve02(0.1, 120)
    curve02(0.010, 105)
    p.left(10)
    curve02(0.2, 110)
    p.left(60)
    curve02(0.3, 138)
    p.left(30)
    curve02(0.2, 160)
    p.right(150)
    curve01(0.2, 100)
    curve01(0.1, 150)
    p.forward(70)
    curve01(0.4, 40)
    p.right(160)
    curve02(0.1, 60)
    p.right(7)
    curve02(0.1, 120)
    curve02(0.2, 30)
    p.forward(20)
    p.left(140)
    curve01(0.2, 40)
    p.left(50)
    curve01(0.2, 70)
    p.left(8)
    curve01(0.1, 70)
    curve01(0.5, 50)
    p.right(153)
    curve02(0.1, 170)
    p.left(81)
    curve01(0.2, 20)
    p.left(3)
    curve01(0.1, 62)
    p.left(153)  # ..
    curve02(0.1, 63)
    p.right(50)
    curve01(0.1, 100)  # 0.1
    p.forward(75)
    p.right(75)
    p.forward(2)
    p.end_fill()
    turtle.done()
    import turtle
    turtle.bgcolor('black')
    p = turtle.Turtle()
    wn = turtle.Screen()
    p.pencolor('red')
    p.hideturtle()

    # curve01
    def curve01(a, d):
        for i in range(d):
            p.right(a)
            p.forward(1)

    # making eye
    p.width(15)
    p.penup()
    p.right(90)
    p.forward(85)
    p.left(90)
    p.forward(35)
    p.pendown()
    p.fillcolor('white')
    p.begin_fill()
    p.left(55)
    curve01(0.09, 100)
    curve01(0.2, 100)
    p.forward(70)
    p.right(90)
    curve01(0.5, 100)
    curve01(00, 30)
    curve01(0.3, 50)
    curve01(0.6, 50)
    p.forward(50)
    p.right(47)
    curve01(0.1, 95)
    p.end_fill()

    # changing
    p.penup()
    p.left(36)
    p.forward(70)
    p.pendown()

    # curve02
    def curve02(a, d):
        for i in range(d):
            p.left(a)
            p.forward(1)

    # second eye
    p.fillcolor('white')
    p.begin_fill()
    p.right(55)
    curve02(0.09, 100)
    curve02(0.2, 100)
    p.forward(70)
    p.left(90)
    curve02(0.5, 100)
    curve02(00, 30)
    curve02(0.3, 50)
    curve02(0.6, 50)
    p.forward(50)
    p.left(47)
    curve02(0.1, 95)
    p.end_fill()

    p.penup()
    p.width(0)
    p.right(49)
    p.forward(30)
    p.left(102)  # 100.40
    p.forward(145)
    p.pencolor('red')

    # making left face
    p.fillcolor('red')
    p.begin_fill()
    p.speed(0)
    p.pendown()
    p.left(90)
    curve01(5, 20)
    p.left(175)
    p.forward(50)
    p.left(25)
    p.forward(28)
    p.right(160)
    p.forward(170)
    curve02(0.2, 65)
    p.right(60)
    curve01(0.1, 140)
    curve01(0.5, 50)
    p.left(180)
    curve02(0.2, 150)
    curve02(0.1, 95)
    p.left(127)
    p.forward(5)
    curve01(2, 20)
    p.right(30)
    p.forward(90)
    p.right(7)
    p.forward(75)
    p.right(160)
    p.forward(100)
    curve02(0.1, 105)
    p.right(70)
    curve01(0.2, 200)
    curve01(0.3, 70)
    p.left(175)
    curve02(0.2, 150)
    curve02(0.3, 150)
    p.forward(20)
    p.left(65)
    curve01(0.1, 120)
    curve01(0.010, 105)
    p.right(10)
    curve01(0.2, 110)
    p.right(60)
    curve01(0.3, 138)
    p.right(30)
    curve01(0.2, 160)
    p.left(150)
    curve02(0.2, 100)
    curve02(0.1, 150)
    p.forward(70)
    curve02(0.4, 40)
    p.left(160)
    curve01(0.1, 60)
    p.left(7)
    curve01(0.1, 120)
    curve01(0.2, 30)
    p.forward(20)
    p.right(140)
    curve02(0.2, 40)
    p.right(50)
    curve02(0.2, 70)
    p.right(8)
    curve02(0.1, 70)
    curve02(0.5, 50)
    p.left(153)
    curve01(0.1, 170)
    p.right(81)
    curve02(0.2, 20)
    p.right(3)
    curve02(0.1, 62)
    p.right(153)  # ..
    curve01(0.1, 63)
    p.left(50)
    curve02(0.1, 175)
    p.left(60)
    p.forward(7)
    p.end_fill()

    # going to replicate
    p.left(92.15)
    p.penup()
    p.forward(417)
    p.pendown()

    p.fillcolor('red')
    p.begin_fill()
    # right face
    p.right(90)
    curve02(5, 20)
    p.right(175)
    p.forward(50)
    p.right(25)
    p.forward(28)
    p.left(160)
    p.forward(170)
    curve01(0.2, 65)
    p.left(60)
    curve02(0.1, 140)
    curve02(0.5, 50)
    p.right(180)
    curve01(0.2, 150)
    curve01(0.1, 95)
    p.right(127)
    p.forward(5)
    curve02(2, 20)
    p.left(30)
    p.forward(90)
    p.left(7)
    p.forward(75)
    p.left(160)
    p.forward(100)
    curve01(0.1, 105)
    p.left(70)
    curve02(0.2, 200)
    curve02(0.3, 70)
    p.right(175)
    curve01(0.2, 150)
    curve01(0.3, 150)
    p.forward(20)
    p.right(65)
    curve02(0.1, 120)
    curve02(0.010, 105)
    p.left(10)
    curve02(0.2, 110)
    p.left(60)
    curve02(0.3, 138)
    p.left(30)
    curve02(0.2, 160)
    p.right(150)
    curve01(0.2, 100)
    curve01(0.1, 150)
    p.forward(70)
    curve01(0.4, 40)
    p.right(160)
    curve02(0.1, 60)
    p.right(7)
    curve02(0.1, 120)
    curve02(0.2, 30)
    p.forward(20)
    p.left(140)
    curve01(0.2, 40)
    p.left(50)
    curve01(0.2, 70)
    p.left(8)
    curve01(0.1, 70)
    curve01(0.5, 50)
    p.right(153)
    curve02(0.1, 170)
    p.left(81)
    curve01(0.2, 20)
    p.left(3)
    curve01(0.1, 62)
    p.left(153)  # ..
    curve02(0.1, 63)
    p.right(50)
    curve01(0.1, 100)  # 0.1
    p.forward(75)
    p.right(75)
    p.forward(2)
    p.end_fill()
    turtle.done()
    # Source code cited from CodeGyani on YouTube

# batMan logo - Fill in coloring and display letters / add quirk relating to Batman
def batManLogo():
    t = turtle.Turtle()
    t.speed(500)

    window = turtle.Screen()
    window.bgcolor("#000000")
    t.color("yellow")
    turtle.title("YOU ARE BATMAN")


    t.left(90)
    t.penup()
    t.goto(-7 * 20, 0)
    t.pendown()

    for a in range(-7 * 20, -3 * 20, 1):
        x = a / 20
        rel = math.fabs(x)
        y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                    math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
        t.goto(a, y * 20)

    for a in range(-3 * 20, -1 * 20 - 1, 1):
        x = a / 20
        rel = math.fabs(x)
        y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
            math.fabs(rel - 1) / (rel - 1))
        t.goto(a, y * 20)

    t.goto(-1 * 20, 3 * 20)
    t.goto(int(-0.5 * 20), int(2.2 * 20))
    t.goto(int(0.5 * 20), int(2.2 * 20))
    t.goto(1 * 20, 3 * 20)
    print("Batman Logo with Python Turtle")
    for a in range(1 * 20 + 1, 3 * 20 + 1, 1):
        x = a / 20
        rel = math.fabs(x)
        y = (2.71052 + 1.5 - 0.5 * rel - 1.35526 * math.sqrt(4 - (rel - 1) ** 2)) * math.sqrt(
            math.fabs(rel - 1) / (rel - 1))
        t.goto(a, y * 20)

    for a in range(3 * 20 + 1, 7 * 20 + 1, 1):
        x = a / 20
        rel = math.fabs(x)
        y = 1.5 * math.sqrt((-math.fabs(rel - 1)) * math.fabs(3 - rel) / ((rel - 1) * (3 - rel))) * (
                1 + math.fabs(rel - 3) / (rel - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                    math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - rel) / (1 - rel))
        t.goto(a, y * 20)

    for a in range(7 * 20, 4 * 20, -1):
        x = a / 20
        rel = math.fabs(x)
        y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
        t.goto(a, y * 20)

    for a in range(4 * 20, -4 * 20, -1):
        x = a / 20
        rel = math.fabs(x)
        y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(rel - 2) - 1) ** 2)
        t.goto(a, y * 20)

    for a in range(-4 * 20 - 1, -7 * 20 - 1, -1):
        x = a / 20
        rel = math.fabs(x)
        y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(rel - 4) / (rel - 4))
        t.goto(a, y * 20)

    t.penup()
    t.goto(300, 300)
    turtle.done()

# ironMan logo
def ironManLogo():
    import turtle

    ankur1 = [
        [(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
         (-40, -20), (0, -20)],
        [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230),
         (70, 260),
         (40, 120), (0, 120)]]
    ankur2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170),
               (-110, -210),
               (-80, -230), (-64, -210), (0, -210)],
              [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0),
               (130, -40),
               (100, -46), (50, -40), (40, -30), (0, -30)]]
    ankur3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
               (0, -250)],
              [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240),
               (60, -220),
               (0, -220)]]

    turtle.hideturtle()
    turtle.bgcolor('#ba161e')  # Dark Red
    turtle.setup(500, 600)
    turtle.title("YOU ARE IRONMAN")
    ankur1Goto = (0, 120)
    ankur2Goto = (0, -30)
    ankur3Goto = (0, -220)
    turtle.speed(2)

    def logo(a, b):
        turtle.penup()
        turtle.goto(b)
        turtle.pendown()
        turtle.color('#fab104')  # Light Yellow
        turtle.begin_fill()

        for i in range(len(a[0])):
            x, y = a[0][i]
            turtle.goto(x, y)

        for i in range(len(a[1])):
            x, y = a[1][i]
            turtle.goto(x, y)
        turtle.end_fill()

    logo(ankur1, ankur1Goto)
    logo(ankur2, ankur2Goto)
    logo(ankur3, ankur3Goto)
    turtle.hideturtle()
    turtle.done()
    # source code from Ankur Gajurel.

# captainAmerica logo
def captainAmericaLogo():
    import turtle
    import math

    t = turtle.Turtle()
    turtle.title("YOU ARE CAPTAIN AMERICA")

    def ankur(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(0)
        t.pensize(2)
        t.speed(10)

    def golo(r, color):
        x_point = 0
        y_pont = -r
        ankur(x_point, y_pont)
        t.pencolor(color)
        t.fillcolor(color)
        t.begin_fill()
        t.circle(r)
        t.end_fill()

    def paanch(r, color):
        ankur(0, 0)
        t.pencolor(color)
        t.setheading(162)
        t.forward(r)
        t.setheading(0)
        t.fillcolor(color)
        t.begin_fill()
        for i in range(5):
            t.forward(math.cos(math.radians(18)) * 2 * r)  # 2cos18°*r
            t.right(144)
        t.end_fill()
        t.hideturtle()

    if __name__ == '__main__':
        golo(288, 'crimson')
        golo(234, 'snow')
        golo(174, 'crimson')
        golo(114, 'blue')
        paanch(114, 'snow')
        turtle.done()

# wolverine logo




# Miscellaneous code/functions ----------------

# Brief introduction to the game
def introToGame():
    print('=============================================')
    print('WELCOME TO "WHICH HERO ARE YOU?"!!\n\n\n\n\n')
    print('This is a survey that will ask you a series of questions,')
    print('and then determine which superhero resonates the most with you!')
    print('Once the hero is determined, you will be shown a unique graphic')
    print('correspondent with your hero. Hope you get your favorite! ^_^')
    print('=============================================')





# QUESTIONS --------------------------

# Create null list and add values as user provides answers. This will be a centerpiece of the algorithm.
# Did not put in function because it's a universal variable, and will be changed often.
answerList = []

# asks if morning or night person
def firstQuestion():

    print("\n\n\n\n1) ARE YOU A...")
    print("\nA. MORNING PERSON")
    print("B. NIGHT PERSON")

    print("\nHint: Choose letter values (E.G. 'A', 'B')")
    answer1 = input("Enter your answer here: ").upper().strip()

    answerList.append(answer1)


# asks what trait user values most
def secondQuestion():

    print("\n\n\n---------------------------------")
    print("2) WHAT TRAIT DO YOU VALUE THE MOST?")
    print("\nA. STRENGTH")
    print("B. COURAGE")
    print("C. INTELLIGENCE")

    print("\nHint: Choose letter values (E.G. 'A', 'B')")
    answer2 = input("Enter your answer here: ").upper().strip()

    answerList.append(answer2)


# asks favorite color
def thirdQuestion():

    print("\n\n\n---------------------------------")
    print("3) WHAT IS YOUR FAVORITE COLOR?")
    print("\nA. BLUE")
    print("B. RED")
    print("C. BLACK")

    print("\nHint: Choose letter values (E.G. 'A', 'B')")
    answer3 = input("Enter your answer here: ").upper().strip()

    answerList.append(answer3)


# asks weapon of choice
def fourthQuestion():
    print("\n\n\n---------------------------------")
    print("4) WHAT IS YOUR WEAPON OF CHOICE?")
    print("\nA. YOUR OWN TWO HANDS")
    print("B. WEAPONRY SUCH AS KNIVES, SMOKEBOMBS, GRAPPLING HOOKS, ETC")

    print("\nHint: Choose letter values (E.G. 'A', 'B')")
    answer4 = input("Enter your answer here: ").upper().strip()

    answerList.append(answer4)


def fifthQuestion():
    print("\n\n\n---------------------------------")
    print("5) IF YOU COULD HAVE ANY POWER, WHAT WOULD IT BE?")
    print("\nA. SUPERHUMAN HEALING")
    print("B. FLIGHT")
    print("C. TECHNOLOGY/WEAPONRY")

    print("\nHint: Choose letter values (E.G. 'A', 'B')")
    answer5 = input("Enter your answer here: ").upper().strip()

    answerList.append(answer5)

# Created function that compiles all questions in order to make it easier when implementing into main method.
def allQuestions():
    firstQuestion()
    secondQuestion()
    thirdQuestion()
    fourthQuestion()
    fifthQuestion()





# DECISIVE LOGIC --------------------------------------

def gameLogic():

    # SuperMan logic    V <- all answers are "A" and I plan to refactor the options to switch it up.
    if answerList == ["A", "A", "A", "A", "B"] or answerList == ["A", "B", "A", "A", "B"]:
        print("\n\n\nYou are Superman!")
        superManLogo()

    # Spider-Man logic
    elif answerList == ["A", "B", "B", "A", "B"] or answerList == ["B", "B", "B", "A", "C"]: # more expected
        print("\n\n\nYou are Spider-Man!")
        spiderManLogo()     # some sort of error comes up after running successfully...

    # Batman logic
    elif answerList == ["B", "C", "C", "B", "C"]: # some will only have one set of answers.
        print("\n\n\nYou are Batman!")      # I later plan on including this within the turtle graphic.
        batManLogo()

    # Captain America logic
    elif answerList == ["A", "B", "A", "A", "C"] or answerList == ["A", "B", "B", "A", "C"]:
        print("\n\n\nYou are Captain America!")
        captainAmericaLogo()

    # IronMan logo
    elif answerList == ["A", "C", "B", "B", "C"] or answerList == ["B", "C", "B", "B", "C"]:
        print("\n\n\nYou are Iron Man!")
        ironManLogo()




# MAIN AND FINAL FUNCTION -----------------------------

def main():
    introToGame()
    allQuestions()
    gameLogic()


main() # <- runs everything.






# CODE UPDATES / NOTABLE TASKS & DOCUMENTATION
#------------------------------------------------

    # Might create seperate functions to place decisive logic, example given below
        # def batManLogoLogic():
            # if answerList == ["B", "C", "C", "B"]:
            # print("\n\n\nYou are Batman!")
            # batManLogo() <== This is just an example. Thinking about placing the logo code as well in other functions
            # or even other files such as a file specifically for logic or another for logos.

    # Still need to work on logic for Spider-Man, BatMan, Captain America, and Iron Man.

    # Look at how Iron Man graphic says "I am Iron Man" and apply that to every graphic that says "You are *enter name*.
