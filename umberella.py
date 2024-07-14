import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Create a turtle object
umbrella = turtle.Turtle()
umbrella.speed(10)

# Function to draw a filled arc
def draw_arc(radius, extent, color):
    umbrella.color(color)
    umbrella.begin_fill()
    umbrella.circle(radius, extent)
    umbrella.left(180 - extent)
    umbrella.circle(radius, extent)
    umbrella.left(180 - extent)
    umbrella.end_fill()

# Draw the umbrella canopy
umbrella.penup()
umbrella.goto(0, -200)
umbrella.pendown()
umbrella.setheading(90)  # Point the turtle upwards

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in colors:
    draw_arc(200, 60, color)
    umbrella.left(60)

# Draw the umbrella handle
umbrella.penup()
umbrella.goto(0, -200)
umbrella.pendown()
umbrella.color("brown")
umbrella.setheading(-90)  # Point the turtle downwards
umbrella.pensize(5)
umbrella.forward(200)

# Hide the turtle and display the window
umbrella.hideturtle()
turtle.done()
