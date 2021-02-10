from turtle import*
from time import*
setup(650.,350,200,200)
pendown()
pensize(10)
pencolor('green')
 

def draw_clover(radius,rotate):
    for i in range(4):
        direction = i*90
        seth(60+direction+rotate)
        fd(4*radius)
        for j in range(2):
             seth(90+direction+rotate)
             circle(radius,180)
        seth(-60+direction+rotate)
        fd(4*radius)
    seth(-90)
    fd(6*radius)
 
draw_clover(30,45)
sleep(5)
