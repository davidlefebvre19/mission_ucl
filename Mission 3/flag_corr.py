import turtle   # module des graphiques tortue
import math
t = turtle.Turtle()     # créer une nouvelle tortue
t.speed("fastest")      # tracé rapide
wn = turtle.Screen()         # Set up the window and its attributes
wn.title("Flags")

def rectangle(w, h, color ):
    """Get turtle t to draw a rectangle of width w, height h and a given color"""
    for i in range(2):
        t.color(color)
        t.pendown()
        t.begin_fill()
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.end_fill()
        t.penup()

def three_color_flag(w, color1, color2, color3,ori):

    if ori == 1:
        for i in [color1, color2, color3]:
            rectangle(w/2,w,i)
            t.penup()
            t.forward(w/2)
            t.pendown()
        t.penup()
        t.forward(20)
        t.pendown()
    elif ori == 2:
        for i in [color1, color2, color3]:
            rectangle(3*w/2,w/3,i)
            t.penup()
            t.left(90)
            t.forward(w/3)
            t.right(90)
            t.pendown()
        t.penup()
        t.forward(3*w/2)
        t.right(90)
        t.forward(w)
        t.left(90)  
        t.forward(20)
        t.pendown()
            
def belgian_flag():
    three_color_flag(40,"black","yellow","red",1)   
def german_flag():
    three_color_flag(40,"yellow","red","black",2)
def dutch_flag():
    three_color_flag(40,"blue","white","red",2)
def luxemburg_flag():
    three_color_flag(40,"blue","white","pink",2)
def french_flag():
    three_color_flag(40,"blue","white","red",1)

belgian_flag()
german_flag()
dutch_flag()
luxemburg_flag()
french_flag()

def european_flag(w):
    rectangle (w/2*3,w , "blue")
    t.color("yellow")
    t.penup()
    t.forward(w/4*3)
    t.left(90)
    t.forward(w/2)
    t.right(90)
    t.pendown()
    t.forward(w/3) #avancer sur la premierer etoile
    for i in range(12): #boucle pour les 12 etoiles
        etoile()
        t.right(30)
        t.forward(math.sin(30)*(w/6)) #distance entre 2 etoiles, cad base du triangle
        t.left(30)
    
def etoile():
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    c=2
    u=10
    t.right(36)
    for k in range(5):
        t.forward(c*u)
        t.left(144)
    t.penup()
    t.end_fill()
    
 
european_flag(200)


wn.mainloop()
