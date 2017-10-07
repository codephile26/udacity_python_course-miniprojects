import turtle

def draw_kite(some_turtle):
    for i in range(0,2):
        some_turtle.forward(100)
        some_turtle.right(60)
        some_turtle.forward(100)
        some_turtle.right(120)


def draw_flower():    
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    turtle.shape("circle")
    turtle.color("blue")
    turtle.speed(20)
    
    for i in range (0,72):
        draw_kite(turtle)
        turtle.right(5)

    turtle.shape("turtle")
    turtle.right(90)
    turtle.forward(300)
    
    window.exitonclick()

draw_flower()
    
