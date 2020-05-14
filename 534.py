import easygui
import turtle
import math
import time
import datetime
l = easygui.ynbox('', 'Codemao', ('是', '否'))
k=False
f = 0
Pn = turtle.Pen()
Pen = turtle.Pen()
Pn.penup()
Pen.penup()
Pn.goto((-300), 0)
Pen.goto((-175), 75)
Pen.hideturtle()
Pn.shape('turtle')
if not l:
    Pen.write('Turtle', font=('Arial', 108, 'italic'))
while True:
    if k:
        t = datetime.time.microsecond
    f1 = ((f % 4) / 2)
    f3 = ((f % 4) % 2)
    F = f1**0.5 if f3==1 else(f1+2)**0.5
    Pn.forward(1+F)
    f += 1
    if k:
        m = datetime.time.microsecond
        n=m-t
    if l:
        #print(f, " ", f1, " ", f3, " ", str(F)[:5],end="    ")
        #print(str(1+F)[:5],)
        Pen.clear()
        Pen.write(str(1+F)[:5], font=('Arial', 108, 'italic'))
    if k:
        print(n.microsecond/1000)
