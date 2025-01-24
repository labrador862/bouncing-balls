import tkinter as tk
import random

# initialize window and add title
window = tk.Tk()
window.title("awesome bouncing")

# size variables, change to whatever
width = 1000
height = 500
numBalls = 25
msBetweenFrames = 15

# creates place for balls to bounce within the window
canvas = tk.Canvas(window, width=width, height=height)
canvas['bg'] = "black"
canvas.pack(fill=tk.BOTH, expand=1)

# image file (.png) to use as balls 
ball_image = tk.PhotoImage(file="awesomeface2.png")
image_width = ball_image.width()    # gets width and height of used image
image_height = ball_image.height()  # to improve bounce mechanics

class Ball:
    def __init__(self, canvas, x, y, vspd, hspd, image, image_width, image_height):
        self.x = x          # x coordinate
        self.y = y          # y coordinate
        self.hspd = hspd    # horizontal speed
        self.vspd = vspd    # vertical speed
        self.image = image  # .png to represent a ball
        self.image_width = image_width   # width of png
        self.image_height = image_height # height of png
        
        self.image_instance = canvas.create_image(self.x, self.y, image = ball_image)
    
    # updates ball position     
    def update(self, canvas):
        self.x += self.hspd # x coordinate changes in accordance with the horizontal speed
        self.y += self.vspd # y coordinate changes in accordance with the vertical speed
        canvas.coords(self.image_instance, self.x, self.y)
        
        # if the ball hits the edge of the window,
        # reverse its horizontal or vertical direction
        if(self.x < 0 + self.image_width / 2 or self.x > width - self.image_width / 2): 
            self.hspd *= -1
        if(self.y < 0 + self.image_height / 2 or self.y > height - self.image_height / 2):
            self.vspd *= -1 

# make space for some balls lol 
balls = []

# create specified number of balls
for i in range(0, numBalls):
    x = random.uniform(image_width, width - image_width)    # ensures ball spawns within the borders
    y = random.uniform(image_height, height - image_height) # ^^
    vspd = random.uniform(-5, 5)                            # randomly chooses initial speed and direction
    hspd = random.uniform(-5, 5)                            # ^^
    balls.append(Ball(canvas, x, y, vspd, hspd,             # adds ball to list of balls
                      ball_image, image_width, image_height))

# place the ball in the canvas
def draw():
    for ball in balls:
        ball.update(canvas)              # update the balls' positions
    window.after(msBetweenFrames, draw)  # after a short delay
    
window.after(msBetweenFrames, draw)      # initial placement of all balls
window.mainloop()
