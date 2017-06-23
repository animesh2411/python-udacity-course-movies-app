import turtle

def draw_art():

    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.speed(3)
    brad.shape("turtle")
    brad.color("black")

    brad.left(60)
    brad.forward(100)
    brad.right(120)
    brad.forward(100)
    brad.backward(50)
    brad.right(120)
    brad.forward(50)

    
    a = turtle.Turtle()      #instantiate a new turtle object called 'a'
    a.hideturtle()           #make the turtle invisible
    a.penup()                #don't draw when turtle moves
    a.goto(100,100)       #move the turtle to a location
    a.showturtle()           #make the turtle visible
    a.pendown()              #draw when the turtle moves
    a.goto(100,100)           #move the turtle to a new location    window.exitonclick()

    a.right(90)
    a.forward(100)
    a.backward(50)
    a.left(90)
    a.left(45)
    a.forward(50)
    a.backward(50)
    a.right(90)
    a.forward(50)
    
draw_art()

# brad angie and tom are instances or objects of the class Turtle
