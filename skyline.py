import turtle

Angle = 25

ANGLE = 35

angle = 120
#this draws the rectangle/road.
def road():
    turtle.begin_fill()

    
    turtle.left(180)
    turtle.forward(530)
    turtle.right(270)
    turtle.forward(300)
    turtle.setheading(90)
    turtle.right(90)
    turtle.forward(1100)
    turtle.left(90)
    turtle.forward(300)
    turtle.home()

    turtle.bgcolor("SkyBlue")
    turtle.pensize(4)
    turtle.color("White")
    turtle.fillcolor("dimgray")
    
    
    turtle.end_fill()
#this is the square part of the house
def house(ANGLE, angle, Angle):
    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.home()
     

    

    turtle.color("red")
    turtle.fillcolor("FireBrick")

    turtle.end_fill()
    #this is the trangle to make the roof
def house_roof(ANGLE, angle, Angle):
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(ANGLE)
    turtle.forward(100)
    turtle.right(angle)
    turtle.forward(100)
    turtle.right(Angle)
    turtle.forward(95)
    turtle.right(90)
    turtle.forward(100)
    turtle.home()


    
   

    turtle.end_fill()
def house_2(ANGLE, angle, Angle):
    turtle.begin_fill()
    
    turtle.forward(350)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.right(ANGLE)
    turtle.forward(100)
    turtle.right(angle)
    turtle.forward(100)
    turtle.right(Angle)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    
    



    turtle.color("red")
    turtle.fillcolor("firebrick")

    turtle.end_fill()



     
    



    

def main ():
    road()
    house(ANGLE, angle, Angle)
    house_roof(ANGLE, angle, Angle)
    house_2(ANGLE, angle, Angle)
    
      

    input("press enter to continue or exit...")


main()
