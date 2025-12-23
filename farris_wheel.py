import turtle
import math
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Farris Wheel Pattern")
screen.tracer(0) 

pen1 = turtle.Turtle()
pen1.speed(0)
pen1.hideturtle()
pen1.pensize(3)
screen.colormode(1.0) 

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.hideturtle()
pen2.pensize(2)
pen2.color("white")      

pen3 = turtle.Turtle()
pen3.speed(0)
pen3.hideturtle()
pen3.pensize(2)
pen3.color("white")

# Parameters
points = 55000       
t_max = 2 * math.pi

# Draw all simultaneously
for i in range(points + 1):
    t = i * t_max / points
    
    #Farris wheel equation
    x1 = math.cos(t) + (0.5) * math.cos(7 * t) + (1/3) * math.sin(17 * t)
    y1 = math.sin(t) + (0.5) * math.sin(7 * t) + (1/3) * math.cos(17 * t)
    x1 *= 110 
    y1 *= 110
    #color based on progress
    hue = i / points
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    pen1.color(r, g, b)

    x2 = math.cos(t) + (0.5) * math.cos(7 * t) + (1/3) * math.sin(17 * t)
    y2 = math.sin(t) + (0.5) * math.sin(7 * t) + (1/3) * math.cos(17 * t)
    x2 *= 25 
    y2 *= 25

    x3 = math.cos(t) + (0.5) * math.cos(7 * t) + (1/3) * math.sin(17 * t)
    y3 = math.sin(t) + (0.5) * math.sin(7 * t) + (1/3) * math.cos(17 * t)
    x3 *= 120
    y3 *= 120

    # Move all pens
    if i == 0:
        # Lift pen, go to starting point then lower pen
        pen1.penup()
        pen1.goto(x1, y1)
        pen1.pendown()

        pen2.penup()
        pen2.goto(x2, y2)
        pen2.pendown()

        pen3.penup()   
        pen3.goto(x3, y3)
        pen3.pendown()
    else:
        pen1.goto(x1, y1)
        pen2.goto(x2, y2)
        pen3.goto(x3, y3)

    # Update screen periodically
    if i % 67 == 0:  
        screen.update()

screen.update()
screen.mainloop()