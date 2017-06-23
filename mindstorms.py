import turtle

def draw_shapes():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.speed(1)
    brad.shape("turtle")
    brad.color("black")
    i=1
    while i<5:
        brad.forward(100)
        brad.right(90)
        i=i+1

    angie=turtle.Turtle()
    angie.shape("triangle")
    angie.color("yellow")
    angie.circle(100)

    tom = turtle.Turtle()
    tom.color("blue")
    tom.shape("square")
    tom.forward(100) 
    tom.left(120)
    tom.forward(100)
    tom.left(120)
    tom.forward(100)

    
    
    window.exitonclick()

draw_shapes()

        
