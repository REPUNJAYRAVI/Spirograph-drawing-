import turtle as t
#importing turtle module as t
import random
#importing random module

#assigning tim name to turtle module for better naming
tim = t.Turtle()
#assigning colour mode to turtle
t.colormode(255)
#function for picking the random colours
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#function for drawing the spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
#calling the function
draw_spirograph(5)


