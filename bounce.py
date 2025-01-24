import tkinter as tk
import random

# initialize window and add title
window = tk.Tk()
window.title("awesome bouncing")

# size variables, change to whatever
width = 1000
height = 500
ballSize = 10
numBalls = 75
msBetweenFrames = 12

# creates place for balls to bounce within the window
canvas = tk.Canvas(window, width=width, height=height)
canvas['bg'] = "black"
canvas.pack(fill=tk.BOTH, expand=1)

class Ball:
    def __init__(self, canvas, x, y, vspd, hspd):
        self.x = x          # x coordinate
        self.y = y          # y coordinate
        self.hspd = hspd    # horizontal speed
        self.vspd = vspd    # vertical speed
        self.instance = canvas.create_oval(self.x-ballSize, self.y-ballSize, # draws a circle of
                                           self.x+ballSize, self.y+ballSize, # height and width ballSize
                                           fill="white")
    
    # updates ball position     
    def update(self, canvas):
        self.x += self.hspd # x coordinate changes in accordance with the horizontal speed
        self.y += self.vspd # y coordinate changes in accordance with the vertical speed
        canvas.coords(self.instance,                   
                      self.x-ballSize, self.y-ballSize,     # places the ball in the correct
                      self.x+ballSize, self.y+ballSize)     # position for the next "frame"
        
        # if the ball hits the edge of the window,
        # reverse its horizontal or vertical direction
        if(self.x < 0 + ballSize or self.x > width - ballSize): 
            self.hspd *= -1
        if(self.y < 0 + ballSize or self.y > height - ballSize):
            self.vspd *= -1 

# make space for some balls lol 
balls = []

# create specified number of balls
for i in range(0, numBalls):
    x = random.uniform(ballSize, width - ballSize)  # ensures ball spawns within the borders
    y = random.uniform(ballSize, height - ballSize) # ^^
    vspd = random.uniform(-5, 5)                    # randomly chooses initial speed and direction
    hspd = random.uniform(-5, 5)                    # ^^
    balls.append(Ball(canvas, x, y, vspd, hspd))    # adds ball to list of balls

# place the ball in the canvas
def draw():
    for ball in balls:
        ball.update(canvas)              # update the balls' positions
    window.after(msBetweenFrames, draw)  # after a short delay
    
window.after(msBetweenFrames, draw)      # initial placement of all balls
window.mainloop()
