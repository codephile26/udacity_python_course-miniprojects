import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("yellow")

    brat = turtle.Turtle()
    brat.shape("turtle")
    brat.color("blue")

    i = 0
    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
        i = i+1

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    angie.circle(100)

    kiddo = turtle.Turtle()
    kiddo.shape("circle")
    kiddo.color("green")

    j = 0
    for j in range(0,3):
        kiddo.backward(100)
        kiddo.left(120)


    window.exitonclick()

draw_shapes()
    
    
    
