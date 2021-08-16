import math
import random
import tkinter
from tkinter import font

WIDTH = 1200
HEIGHT = 900
x = 0
y = 0
nx = 0
ny = 0

placements = [0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0,
              0]

class Block(object):
  def __init__(self, canvas, x, y, sz):
    self.x = x
    self.y = y
    self.color = 'snow'
    self.outline = 'gray50'
    self.sz = sz

    sz = self.sz / 2
    self.id = canvas.create_rectangle(
      x - sz, y - sz, x + sz, y + sz, fill=self.color, outline=self.outline)

  def SetXY(self, x, y):
    self.x = x
    self.y = y

  def SetColor(self, color):
    self.color = color

  def Update(self, canvas):
    canvas.itemconfigure(self.id, fill=self.color, outline=self.outline)
    sz = self.sz / 2
    canvas.coords(
      self.id, (self.x - sz, self.y - sz, self.x + sz, self.y + sz))


root = tkinter.Tk()
root.title('Jayden\'s Game')

canvas = tkinter.Canvas(root,
                        bg='sky blue',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

margin = 5
#margin must be less than first number in total_blockside's value interpertation.
total_blocksize = 100 - margin / 2
board = []
block_x = WIDTH / 2 - total_blocksize * 2 - 5
for i in range(4):
  row = []
  block_y = HEIGHT / 2 - total_blocksize * 2 - 5
  for j in range(4):
    row.append(Block(canvas, block_x, block_y, total_blocksize - margin))
    block_y += total_blocksize
  block_x += total_blocksize
  board.append(row)


def MouseClick(event):
  global x, y

  x = event.x
  y = event.y

def MouseUp(event):
  global x, y
  global nx, ny

  nx = event.x
  ny = event.y

 # print(x, y, nx, ny)

  if abs(x - nx) > abs(y - ny):
    if x > nx:
      # left
      place = 0
      for row in board:
        for block in row:
          if not place == 0 or place == 4 or place == 8 or place == 12:
            if placements[place] - 1 == placements[place]:
              placements[place - 1] = placements[place] * 2
              placements[place] = 0
            elif placements[place] - 1 == 0:
              placements[place - 1] = placements[place]
              placements[place] = 0
            place += 1
    elif nx > x:
      # right
      for row in board:
        for block in row:
  elif abs(y - ny) > abs(x - nx):
    if y > ny:
      # up
      for row in board:
        for block in row:
    elif ny > y:
      # down
      for row in board:
        for block in row:


def MouseMove(event):
  block.SetXY(WIDTH - event.x, HEIGHT - event.y)


def check (event):
  for row in board:
    for block in row:
      print(block.x, block.y)


def UpdateUniverse():
  for row in board:
    for block in row:
      block.Update(canvas)
  root.after(50, UpdateUniverse)


canvas.focus_set()
canvas.bind('<ButtonPress-1>', MouseClick)
canvas.bind('<ButtonRelease-1>', MouseUp)
canvas.bind('a', check)

root.after(50, UpdateUniverse)
root.mainloop()
