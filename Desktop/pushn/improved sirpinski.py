import turtle

s=turtle.Screen()
t=turtle.Turtle()
t.speed(speed=0)

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

def sirpenski(t,n,x,y,l,colorit,depth):
    if depth==0 :
        if n==0:
            triangle(t, x, y, l,colorit)
        else :
            colorit="red"
            sirpenski2(t, n - 1, x, y, l / 2,colorit,depth)
            goto(t,x+(l/2), y)
            colorit = "blue"
            sirpenski2(t, n - 1, x+(l / 2), y, l / 2,colorit,depth)
            goto(t,x+(l/4), y+(l/2.3))
            colorit = "magenta"
            sirpenski2(t,n-1, x+(l/4), y+(l/2.3), l/2,colorit,depth)
            goto(t,x, y)
    elif depth < 0 :
        if n==0:
            triangle(t, x, y, l,colorit)
        else :
            sirpenski(t, n - 1, x, y, l / 2,colorit,depth)
            goto(t,x+(l/2), y)
            sirpenski(t, n - 1, x+(l / 2), y, l / 2,colorit,depth)
            goto(t,x+(l/4), y+(l/2.3))
            sirpenski(t,n-1, x+(l/4), y+(l/2.3), l/2,colorit,depth)
            goto(t,x, y)
    else :
        if n == 0:
            triangle(t, x, y, l, colorit)
        else:
            if n==j-depth:
                colorit = "red"
                sirpenski2(t, n - 1, x, y, l / 2, colorit, depth)
                goto(t, x + (l / 2), y)
                colorit = "blue"
                sirpenski2(t, n - 1, x + (l / 2), y, l / 2, colorit, depth)
                goto(t, x + (l / 4), y + (l / 2.3))
                colorit = "magenta"
                sirpenski2(t, n - 1, x + (l / 4), y + (l / 2.3), l / 2, colorit, depth)
                goto(t, x, y)
            else:
                sirpenski(t, n - 1, x, y, l / 2, colorit, depth)
                goto(t, x + (l / 2), y)
                sirpenski(t, n - 1, x + (l / 2), y, l / 2, colorit, depth)
                goto(t, x + (l / 4), y + (l / 2.3))
                sirpenski(t, n - 1, x + (l / 4), y + (l / 2.3), l / 2, colorit, depth)
                goto(t, x, y)


def sirpenski2(t,n,x,y,l,colorit,depth):
    if n==0:
        triangle(t, x, y, l,colorit)
    else :
        sirpenski2(t, n - 1, x, y, l / 2,colorit,depth)
        goto(t,x+(l/2), y)
        sirpenski2(t, n - 1, x+(l / 2), y, l / 2,colorit,depth)
        goto(t,x+(l/4), y+(l/2.3))
        sirpenski2(t,n-1, x+(l/4), y+(l/2.3), l/2,colorit,depth)
        goto(t,x, y)

n=3
j=n
b=n
x=0
y=0
l=300
sirpenski(t,n,x,y,l,colorit="black",depth=2)
turtle.mainloop()

