import tkinter as tk
import random

window = tk.Tk()
window.title("awesome bouncing")

width = 1000
height = 500
ballSize = 10
numBalls = 75

canvas = tk.Canvas(window, width=width, height=height)
canvas['bg'] = "black"
canvas.pack(fill=tk.BOTH, expand=1)

class Ball:
    def __init__(self, canvas, x, y, vspd, hspd):
        self.x = x
        self.y = y
        self.vspd = vspd
        self.hspd = hspd
        self.instance = canvas.create_oval(self.x-ballSize, self.y-ballSize, self.x+ballSize, self.y+ballSize, fill="white")
        
    def update(self, canvas):
        self.x += self.hspd
        self.y += self.vspd
        canvas.coords(self.instance, self.x-ballSize, self.y-ballSize, self.x+ballSize, self.y+ballSize)
        
        if(self.x < 0 + ballSize or self.x > width - ballSize):
            self.hspd *= -1
        if(self.y < 0 + ballSize or self.y > height - ballSize):
            self.vspd *= -1    
balls = []

for i in range(0,numBalls):
    x = random.uniform(ballSize, width - ballSize)
    y = random.uniform(ballSize, height - ballSize)
    vspd = random.uniform(-4, 4)
    hspd = random.uniform(-4, 4)
    balls.append(Ball(canvas, x, y, vspd, hspd))
    
def draw():
    for ball in balls:
        ball.update(canvas)
    window.after(15, draw)
    
window.after(15, draw)
window.mainloop()
