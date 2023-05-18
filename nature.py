import turtle
t=turtle.Turtle()
s=turtle.Screen()

s.bgcolor("light yellow")
t.pensize(6)
s.title("nature view")
from pygame import mixer
mixer.init()

 
mixer.music.load("C://Users//hp//Downloads//nature.mp3")
mixer.music.play()
#t.speed(10)

def hill():
    t.begin_fill()
    t.fillcolor("brown")
    for i in range(6):
        t.setheading(0)
        t.left(40)
 
        t.fd(200)
        t.setheading(270)
        t.right(310)
        t.fd(200)
    t.end_fill()

    
 

t.up()
t.goto(-770,250)
t.down()

t.color("black")
hill()
t.setheading(180)
t.fd(1835)
 
"""
t.setheading(0)
t.left(40)
 
t.fd(200)
t.setheading(270)
t.right(310)
t.fd(200)

"""
t.up()
t.setheading(0)
t.left(13)
t.fd(246)

#sun
t.down()
t.color("orange")
#t.begin_fill()
#t.fillcolor("yellow")
t.circle(-147,extent=45)
#t.end_fill()
t.setheading(90)
t.right(40)
t.fd(140)
t.bk(140)

def sunraise1():
    t.up()
    t.setheading(180)
    t.fd(20)
    t.setheading(90)
    t.fd(10)
    t.down()

sunraise1()
t.right(20)
t.fd(140)
t.bk(140)

sunraise1()
t.right(10)
t.fd(120)
t.bk(120)

def sunraise2():
    t.up()
    t.setheading(180)
    t.fd(20)
    t.setheading(90)
    t.down()


sunraise2()
t.left(20)
t.fd(100)
t.bk(100)

sunraise2()
t.left(40)
t.fd(120)
t.bk(120)

sunraise2()
t.left(52)
t.fd(140)
t.bk(140)

#home
t.up()
t.goto(-200,0)

#triangle
t.color("black")
 
t.begin_fill()
t.fillcolor("pink")
t.down()
t.setheading(270)
t.right(45)
t.fd(200)
t.bk(200)
t.end_fill()

t.setheading(270)
t.left(45)
t.fd(200)

# gate box
#t.color("red")
t.begin_fill()
t.fillcolor("pink")
t.setheading(180)
t.fd(282)

t.setheading(270)
t.fd(250)
t.setheading(0)
t.fd(282)

t.setheading(90)
t.fd(250)
t.end_fill()

#rectangle up
#t.color("yellow")
t.begin_fill()
t.fillcolor("pink")
t.setheading(0)
t.fd(300)
t.setheading(90)
t.fd(140)
t.setheading(180)
t.fd(444)
#t.end_fill()

# circle in home
t.color("blue")

t.setheading(270)
t.up()
t.fd(50)
t.down()
t.begin_fill()
t.fillcolor("blue")
t.circle(10)
t.end_fill()
t.up()
t.setheading(90)
t.fd(50)
t.down() 

#lining in ractangle up

k=50
def line():
    t.color("purple")
    for i in range(13):
        global k
        if i==10 or i>10:
            t.setheading(0)
            t.fd(30)
            t.setheading(270)
            t.left(45)
             
            t.fd(200-k)
            t.bk(200-k)
            k=k+43

        else:

            t.setheading(0)
            t.fd(30)
            t.setheading(270)
            t.left(45)
            t.fd(200)
            t.bk(200)


            



line()

# ractangle down
t.color("black")
#t.begin_fill()
#t.fillcolor("blue")
t.setheading(0)
t.fd(55)
t.setheading(270)
t.fd(140)
t.fd(247)
t.setheading(180)
t.fd(300)
#t.end_fill()


# gate
t.color("brown")
#t.begin_fill()
#t.fillcolor("yellow")
t.up()
t.goto(-175,-300)
t.down()
t.setheading(270)
t.fd(100)
t.setheading(180)
t.fd(70)
t.setheading(90)
t.fd(100)
t.circle(-35,extent=180)
 

#### ggggg
t.setheading(270)
t.right(30)
t.fd(55)

t.setheading(270)
t.left(30)
t.fd(55)

t.setheading(180)
t.fd(70)
t.setheading(90)
t.right(30)
t.fd(55)

t.setheading(90)
t.left(30)
t.fd(55)
#t.end_fill()

## window
t.color("purple")
t.up()
t.setheading(0)
t.fd(300)

t.down()
t.begin_fill()
#t.fillcolor("purple")
for i in range(4):
    
    t.fd(50)
    t.left(90)
t.end_fill()


# railing
t.color("brown")
t.up()
t.fd(190)
t.setheading(90)
t.fd(20)
t.setheading(0)


t.down()
#t.fd(300)
def railing(n):
    for i in range(n):
        t.fd(40)
        t.setheading(270)
        t.fd(100)
        t.bk(100)
        t.setheading(0)

railing(6)

t.setheading(270)
t.up()
t.fd(100)
t.down()
t.setheading(180)
t.fd(240)
t.bk(240)


## tree
def tree():
    t.setheading(0)
    t.fd(40)
    t.setheading(90)
    #t.begin_fill()
    #t.fillcolor("light brown")
    t.fd(300)
    #t.end_fill()
    t.begin_fill()
    t.fillcolor("#228B22")
    t.setheading(180)
    t.circle(-60,extent=120)
    t.setheading(90)
    t.left(30)
    t.circle(-45,extent=140)
    t.setheading(0)
    t.left(60)
    t.circle(-45,extent=170)
    t.setheading(270)
    t.left(80)
    t.circle(-35,extent=140)

    t.setheading(0)
    t.right(78)
    t.circle(-45,extent=100)
    
#-----------------
    t.up()
    t.fd(52)
    t.bk(52)

    t.end_fill()
    t.down()
#  3333333333
     
    t.begin_fill()
    t.fillcolor("#A0522D")
    t.setheading(270)
    t.fd(300)

    t.setheading(180)
    t.fd(51)
    #------------
    t.setheading(90)
    t.fd(303)

    t.end_fill()
    t.bk(300)
     
    #-----------------

    

    t.setheading(90)
    t.fd(103)
    t.setheading(180)
    t.fd(40)


tree()

# after the tree
t.up()
t.setheading(0)
t.fd(50)
t.down()
railing(5)

t.setheading(270)
t.fd(100)
t.setheading(180)
t.fd(163)

##-----------railing and tree
t.up()
t.fd(1340)

t.down()
t.setheading(90)
t.fd(55)
railing(9)
t.setheading(270)
t.fd(100)
tree()
t.setheading(270)
t.fd(100)
t.setheading(180)
t.fd(320)

