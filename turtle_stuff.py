import turtle

ANGLE = 45 
pencolor = 23
fillcolor = 32

def test_drive():
    turtle.forward(100)
    turtle.left(64)
    turtle.setheading(137)
    turtle.down()
    turtle.goto(50, 50)
    turtle.home()
    turtle.circle(25)
def turtle_state ():
    print("turtle is down:", turtle.isdown())
    print("turtle heading:", turtle.heading())
    print("turtle X,Y:", turtle.xcor() , turtle.ycor())

def square(size, ANGLE, pencolor, fillcolor):

    turtle.pensize(4)
    turtle.color("red")
    turtle.fillcolor("blue")
    turtle.begin_fill()
    
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.right(ANGLE)
    
turtle.begin_fill()

    

def main ():
    # test_drive()
    turtle_state()
    length = 200
    square(ANGLE, 157, "red", "green")
    square (100, 113, "fuchsia", "yellow") 
    square (90, 76, "dark orchid", "FireBrick")
    turtle.bgcolor("pink")
    turtle_state()

      

    input("press enter to continue or exit...")


main()


