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


def CheckHit():
  global bad_guys
  global bullets

  new_bullets = []
  for t in bullets:
    hit_something = False

    for g in bad_guys:
      if g.IsDone():
        # If this bad guys has already been eliminated. Skip.
        continue

      if g.Intersect(t):
        # Mark it that the bullet hit something.
        hit_something = True
        # Also mark the bad guy that it has been hit once.
        g.Hit(canvas)
        break

    if hit_something:
      # Bullet goes away after hitting something.
      t.Delete(canvas)
    else:
      new_bullets.append(t)
  bullets = new_bullets

  # Now, let's delete all the dead bad guys from the screen.
  new_bad_guys = []
  for g in bad_guys:
    if g.IsDone():
      g.Delete(canvas)
    else:
      new_bad_guys.append(g)
  bad_guys = new_bad_guys


def Update():
  global bad_guys
  global bullets

  MaybeAddBadGuy()

  bad_guys = Next(bad_guys)
  bullets = Next(bullets)

  CheckHit()

  root.after(50, Update)


canvas.bind('<Motion>', Aim)
canvas.bind('<ButtonPress-1>', Fire)

root.after(50, Update)

root.mainloop()
