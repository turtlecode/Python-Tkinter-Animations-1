from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 1000
HEIGHT = 1000

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"pink")
tennis_ball = Ball(canvas,0,0,50,4,3,"purple")
basket_ball = Ball(canvas,0,0,125,3,5,"orange")
bowling_ball = Ball(canvas,0,0,75,2,1,"black")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()