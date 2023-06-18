# turtle library
import turtle

# This to make turtle object
tess = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600, 600)
# self defined function to print coordinate


def buttonclick(x,y):
	print("You clicked at this coordinate({0},{1})".format(x,y))


# onscreen function to send coordinate

turtle.onscreenclick(buttonclick,1)
turtle.listen() # listen to incoming connections
turtle.speed(10) # set the speed
turtle.done() # hold the screen
