import math
import random
import tkinter
from tkinter import font

WIDTH = 1200
HEIGHT = 900

class Block(object):
  COLORS = ['red',
            'orange',
            'gold',
            'yellow',
            'green',
            'turquoise',
            'blue',
            'purple',
            'black']
  SIZE = 10

  def __init__(self, canvas, x, y):
    self.x = x
    self.y = y
    self.color = random.choice(Block.COLORS)

    sz = Block.SIZE
    self.id = canvas.create_oval(
      x - sz, y - sz, x + sz, y + sz, fill=self.color, outline=self.color)

  def SetXY(self, x, y):
    self.x = x
    self.y = y

  def SetColor(self, color):
    self.color = color

  def Update(self, canvas):
    canvas.itemconfigure(self.id, fill=self.color, outline=self.color)
    sz = Block.SIZE
    canvas.coords(
      self.id, (self.x - sz, self.y - sz, self.x + sz, self.y + sz))


root = tkinter.Tk()

canvas = tkinter.Canvas(root,
                        bg='white',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

block = Block(canvas, 0, 0)


def MouseClick(event):
  block.SetColor(random.choice(Block.COLORS))


def MouseMove(event):
  block.SetXY(event.x, event.y)


def KeyPress(event):
  print(event.char)


def UpdateUniverse():
  block.Update(canvas)
  root.after(50, UpdateUniverse)


canvas.focus_set()
canvas.bind('<Motion>', MouseMove)
canvas.bind('<ButtonPress-1>', MouseClick)
canvas.bind('<KeyPress>', KeyPress)

root.after(50, UpdateUniverse)
root.mainloop()
