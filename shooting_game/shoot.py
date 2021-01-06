import constants as c
import math
import objects
import random
import tkinter
from tkinter import font

root = tkinter.Tk()

canvas = tkinter.Canvas(root,
                        bg='white',
                        height=c.HEIGHT,
                        width=c.WIDTH)
canvas.pack()

level = 1
bad_number_defeated = 0

bunker = objects.Bunker(canvas)
bad_guys = []
bullets = []

def MakeBadGuy():
  badslope = Slope(c.CENTER_X, c.CENTER_Y, line.x, line.y)
  bunker.Next(canvas, slope)
  id = canvas.create_square(badrandom_x,
                            badrandom_y,
                            badrandom_x2,
                            badrandom_y2)
  id = canvas.create_line(badrandom_x + 10,
                          badrandom_y + 10,
                          badrandom_x - 10,
                          badrandom_y - 10)

def Slope(x1, y1, x2, y2):
  return math.atan2(y2 - y1, x2 - x1)

def Aim(event):
  # Calculate new endpoint of the line.
  slope = Slope(c.CENTER_X, c.CENTER_Y, event.x, event.y)
  bunker.Next(canvas, slope)

def Fire(event):
  bullets.append(objects.Bullet(canvas,
                                c.CENTER_X, c.CENTER_Y,
                                Slope(c.CENTER_X, c.CENTER_Y, event.x, event.y),
                                5.0 + 2.0 * (random.random())))

def MaybeAddBadGuy():
  global bad_guys

  if random.random() < 0.015:
    bad_guys.append(objects.BadGuy(canvas, 2, 10))


def Next(l):
  new_l = []
  for o in l:
    o.Next(canvas)
    if o.IsDone():
      o.Delete(canvas)
    else:
      new_l.append(o)
  return new_l


def Update():
  global bad_guys
  global bullets

  MaybeAddBadGuy()

  bad_guys = Next(bad_guys)
  bullets = Next(bullets)

  root.after(50, Update)


canvas.bind('<Motion>', Aim)
canvas.bind('<ButtonPress-1>', Fire)

root.after(50, Update)

root.mainloop()
