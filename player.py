from tkinter import *
from utils.tkinter_png import *

class Player:
  def __init__(self, canvas):
    self.x = 400
    self.y = 500 - 115 # player stays in the same Y coordinate
    self.walk_to_x = self.x
    self.walk_speed = 10 # pixels per second
    self.player_img = PngImageTk('assets/player.png')
    self.player_img.convert()

  def update_state(self):
    if abs(self.x - self.walk_to_x) <= self.walk_speed:
      # not moving
      return
    elif self.x < self.walk_to_x:
      self.x = self.x + self.walk_speed
    else:
      self.x = self.x - self.walk_speed

  def set_walk_to(self, x):
    self.walk_to_x = x

  def render(self, canvas):
    canvas.create_image(self.x, self.y, image=self.player_img.image, anchor=S)