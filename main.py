import random
import colorgram
import turtle as turtle_module

# to use your own colors with color gram simply find an image and place it in this folder
# uncomment lines 12-23 and comment out the rest of the code starting at line 27
# use color gram.extract('your image name goes here', number of how many colors to pull)
# the loop I wrote starting at 16 will fill rgb colors with your colors and when you run the code they will print
# copy your new colors and paste them in colors on line 27 to replace mine, or make more new lists
# when done getting colors comment this back out and run the program, pay attention to the prompts in the CLI
#
# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 12)
#
# for each in colors:
#     r = each.rgb.r
#     g = each.rgb.g
#     b = each.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#print(rgb_colors)
#


colors = [(14, 38, 26), (18, 15, 11), (42, 122, 86), (18, 91, 60), (13, 27, 33), (108, 188, 154), (60, 165, 127), (183, 245, 217), (126, 228, 194), (16, 12, 14), (98, 101, 63), (174, 164, 119)]

t = turtle_module
screen = turtle_module.Screen()
turtle_module.colormode(255)
screen.setup(width=1010, height=1020)

t.penup()
t.goto(-450, -470)
t.pendown()
t.shape('circle')
t.shapesize(stretch_wid=2, stretch_len=2)
t.speed(5)


def go_across(times_to_repeat):
    for _ in range(times_to_repeat):
        t.color(random.choice(colors))
        t.stamp()
        t.penup()
        t.forward(100)
        t.pendown()
        t.stamp()

def up_and_left():
    t.setheading(90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.setheading(180)

def up_and_right():
    t.setheading(90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.setheading(0)


number_across = int(input('How many dots would you like to stamp across?\n'))
number_up = int(input('how many dots high would you like to go (for best results choose numbers evenly divisible by 2)?\n'))

number_across = number_across - 1
number_up = number_up / 2

for _ in range(int(number_up)):
    go_across(int(number_across))
    up_and_left()
    go_across(int(number_across))
    up_and_right()

t.color('white')

screen.exitonclick()













