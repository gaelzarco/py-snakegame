import turtle

WIDTH = 500
HEIGHT = 500

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Program Title")
screen.bgcolor("black")

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_turtle.color('white')

my_turtle.forward(100)

turtle.done()