import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    #drwa square
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.speed(3)
    brad.shape("turtle")
    brad.color("black")
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
        
    #draw circle
    #angie=turtle.Turtle()
    #angie.shape("triangle")
    #angie.color("yellow")
    #angie.circle(100)

    #draw triangle 
    #tom = turtle.Turtle()
    #tom.color("blue")
    #tom.shape("square")
    #tom.forward(100) 
    #tom.left(120)
    #tom.forward(100)
    #tom.left(120)
    #tom.forward(100)

    window.exitonclick()

draw_art()

# brad angie and tom are instances or objects of the class Turtle
