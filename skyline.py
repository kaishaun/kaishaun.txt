import turtle

#this draws the rectangle
def rectangle_draw():
    turtle.color("gold")
    turtle.fillcolor("DarkRed")
    turtle.begin_fill()
    

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(150)
    turtle.setheading(90)
    turtle.left(90)
    turtle.forward(150)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.home()
     
    

turtle.begin_fill()

    

def main ():
    rectangle_draw()
    
      

    input("press enter to continue or exit...")


main()
