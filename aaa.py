import turtle
from time import sleep
nodesize = 3
connectionsize = 1
actual = False
shownames = True
p = turtle.Pen()
p.penup()


def ellipse(x, y, w):
    p.penup()
    p.goto(x, y)
    p.pendown()
    p.begin_fill()
    p.circle(w)
    p.end_fill()


def typetosizefactor(n):
    if actual:
        return {'C': 1, 'Si': 2, 'N': 1.3, 'P': 2.3, 'O': 1.6, 'S': 2.6, 'Se': 3.6, 'Na': 1.9, 'K': 2.9, 'Ca': 2.1, 'H': 0.3}[n]
    else:
        return {'C': 2.5, 'Si': 2, 'N': 1.5, 'P': 2.5, 'O': 1.5, 'S': 1.7, 'Se': 1.8, 'Na': 0.9, 'K': 0.9, 'Ca': 1.5, 'H': 0.3}[n]


class atom:
    def __init__(self, x, y, typ):
        self.x = x
        self.y = y
        self.typ = typ

    def draw(self):
        ellipse(self.x, self.y, typetosizefactor(self.typ)*nodesize)
        if shownames:
            p.pencolor('white')
            p.write(self.typ)
            p.pencolor('black')


class bond:
    def __init__(self, one, two):
        self.x1 = atoms[one].x
        self.y1 = atoms[one].y
        self.bondlength = (typetosizefactor(atoms[one].typ) +
                           typetosizefactor(atoms[two].typ))/2*connectionsize
        self.x2 = atoms[two].x
        self.y2 = atoms[two].y

    def draw(self):
        p.pensize(self.bondlength)
        p.penup()
        p.goto(self.x1, self.y1)
        p.pendown()
        p.goto(self.x2, self.y2)


atoms = [atom(0, 0, 'C'), atom(0, 50, 'C')]
bonds = [bond(0,1)]
sleep(1)
for i in bonds:
    i.draw()
sleep(1)
for i in atoms:
    i.draw()

p.penup()
p.hideturtle()
turtle.exitonclick()
