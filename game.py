from tkinter import *
from utils.tkinter_png import *
from player import Player

class Game:
  def __init__(self, root):
    self.root = root
    self.setup_canvas()

    # setup game objects
    self.player = Player(self.canvas)
    self.background_photo = PngImageTk('assets/background.png')
    self.background_photo.convert()

    # run the game
    self.gameloop()

  def setup_canvas(self):
    self.canvas = Canvas(self.root, width=800, height=500, bd=0)
    self.canvas.place(x=0, y=0)
    self.canvas.pack()
    self.canvas.bind('<Button-1>', self.handle_click)

  def draw_background(self):
    self.canvas.create_image(0, 0, image=self.background_photo.image, anchor=NW)

  def handle_click(self, event):
    self.player.set_walk_to(event.x)

  def gameloop(self):
    # clear canvas
    self.canvas.destroy()
    self.setup_canvas()

    # update states
    self.player.update_state()

    # draw
    self.draw_background()
    self.player.render(self.canvas)
    self.root.after(10, self.gameloop)