Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
from random import randint
turtle.getscreen()
<turtle._Screen object at 0x000002639F192080>
t = turtle.Turtle()
t.speed(-1)
turtle.colormode(255)

for i in range(360)
SyntaxError: expected ':'
for i in range(360):
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    t.pencolor((r,g,b))
    t.fd(200)
    t.bk(randint(0,20))
    t.lt(1)






    
