import turtle
import math
t = turtle.Turtle()  
t.speed("fastest")
wn = turtle.Screen()
wn.title("Flags") 
t.shape("turtle")

def basic_flag (width, height, color):
    for i in range(2):
        t.color(color)
        t.pendown()
        t.begin_fill()
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.end_fill()
        t.penup()

def three_color_flag (width, height, color1, color2, color3, ori):
	# rect vert
	colors = []
	colors.append(color1)
	colors.append(color2)
	colors.append(color3)
	if ori == 1:
		for color in colors:
			basic_flag(width*2/3, height, color)
			t.forward(width*2/3)
	else:
		for color in colors:
			basic_flag(width, height*2/3, color)
			t.right(90)
			t.forward(height*2/3)
			t.left(90)

def star(size):
	t.color("yellow")
	t.pendown()
	t.begin_fill()
	for i in range (5):
		t.forward(size)
		t.right(144)
	t.end_fill()
	t.penup()
	t.right(18)
	t.forward(size/2)
	t.left(18)



def european_flag (width, height, size):
	basic_flag(width, height, "blue")
	t.forward(width/2)
	t.right(90)
	t.forward(height/2)
	t.right(90)
	for i in range (12):
		t.forward(height/2-25)
		star(size)
		t.left(180)
		t.forward(height/2-25)
		t.right(30)


def belgian_flag():
	three_color_flag(30,20,"black", "yellow", "red", 1)





european_flag(350, 200, 20)


wn.mainloop()
