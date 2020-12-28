import turtle

s=turtle.Screen()
t=turtle.Turtle()
t.speed(speed=0)

x=0
y=0
l=300

def goto(t,x,y):
    t.penup()
    t.setx(x)
    t.sety(y)
    t.pendown()

def triangle(t,x,y,l,colorit):
    t.setheading(0)
    t.pencolor(colorit)
    t.forward(l)
    t.setheading(120)
    t.forward(l)
    t.setheading(240)
    t.forward(l)
    goto(t,x, y)

def sirpenski(t,n,x,y,l,colorit):
    if n==0:
        triangle(t, x, y, l,colorit)
    else :
        colorit="red"
        sirpenski2(t, n - 1, x, y, l / 2,colorit)
        goto(t,x+(l/2), y)
        colorit = "green"
        sirpenski2(t, n - 1, x+(l / 2), y, l / 2,colorit)
        goto(t,x+(l/4), y+(l/2.3))
        colorit = "blue"
        sirpenski2(t,n-1, x+(l/4), y+(l/2.3), l/2,colorit)
        goto(t,x, y)

def sirpenski2(t,n,x,y,l,colorit):
    if n==0:
        triangle(t, x, y, l,colorit)
    else :
        #t.setheading(0)
        sirpenski2(t, n - 1, x, y, l / 2,colorit)
        #t.setheading(0)
        goto(t,x+(l/2), y)
        sirpenski2(t, n - 1, x+(l / 2), y, l / 2,colorit)
        #t.setheading(0)
        goto(t,x+(l/4), y+(l/2.3))
        sirpenski2(t,n-1, x+(l/4), y+(l/2.3), l/2,colorit)
        goto(t,x, y)

#triangle(t,x,y,l,"black")
sirpenski(t,4,x,y,l,colorit="black")
#goto(t,10,10)
turtle.mainloop()

