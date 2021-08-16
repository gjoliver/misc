import math
import random
import tkinter
from tkinter import font

WIDTH = 1200
HEIGHT = 900


class Block(object):
  def __init__(self, canvas, x, y, z, xdif):
    self.x = x - xdif
    self.y = y
    self.z = z / 45
    self.color = 'snow'
    self.outline = 'gray50'
    self.xdif = xdif

    sz = self.z
    self.id = canvas.create_rectangle(
      x - sz, y - sz, x + sz, y + sz, fill=self.color, outline=self.outline)

  def SetXY(self, x, y):
    self.x = x
    self.y = y

  def SetColor(self, color):
    self.color = color

  def Update(self, canvas):
    canvas.itemconfigure(self.id, fill=self.color, outline=self.outline)
    sz = self.z * 45
    canvas.coords(
      self.id, ((self.x - self.xdif - sz) * self.z, (self.y - sz) * self.z, (self.x - self.xdif + sz) * self.z, (self.y + sz) * self.z))


root = tkinter.Tk()
root.title('Jayden\'s Game')

canvas = tkinter.Canvas(root,
                        bg='sky blue',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

block = Block(canvas, 0, 0, 5, 0)


def MouseClick(event):
  block.SetColor(random.choice(Block.COLORS))


def MouseMove(event):
  block.SetXY(WIDTH - event.x, HEIGHT - event.y)


def Up():
  block.z += 2


def Down():
  block.z -= 2


def Left():
  block.xdif -= 5


def Right():
  block.xdif += 5

def check():
  print(block.x * block.z / 45, block.y * block.z / 45, block.z)

def KeyPress(event):
  comsumableLetters = {
    'w': Up,
    'a': Left,
    's': Down,
    'd': Right,
    'c': check
  }
  if event.char in comsumableLetters:
    comsumableLetters[event.char]()


def UpdateUniverse():
  block.Update(canvas)
  root.after(50, UpdateUniverse)


canvas.focus_set()
canvas.bind('<Motion>', MouseMove)
canvas.bind('<ButtonPress-1>', MouseClick)
canvas.bind('<KeyPress>', KeyPress)

root.after(50, UpdateUniverse)
root.mainloop()
