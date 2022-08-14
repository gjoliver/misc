import tkinter
import math

WIDTH = 1200
HEIGHT = 900


class Line(object):
  def __init__(self, canvas, x0, y0, x1, y1):
    self.x0 = x0
    self.y0 = y0
    self.x1 = x1
    self.y1 = y1
    self.id = canvas.create_line(self.x0, self.y0, self.x1, self.y1, width = 10)

  def update(self, canvas, x, y):
    self.x0 += x
    self.y0 += y
    self.x1 += x
    self.y1 += y
    canvas.move(self.id, x,y)

  def setcoordsy(self, canvas, x0, y0, x1, y1):
    canvas.coords(self.id, self.x0, y0, self.x1, y1)

  def destruct(self, canvas):
    canvas.delete(self.id)


root = tkinter.Tk()
root.title('platformer')

canvas = tkinter.Canvas(root,
                        bg='white',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

level = 1
before_level = 0

level1x = [0, 1200]
level1y = [800, 800]

lines_id = []


world_x = 0
world_y = 0

collision_walls =[]

gravity = 0
jump = 0

#in this world, everything moves around the player(circle).
canvas.create_oval(10, 435, 40, 465, fill='red')

def UpdateUniverse():
  global level
  global before_level

  if not level == before_level:
    # list.clear() didn't work.
    for i in range(len(lines_id)):
      lines_id[0].destruct(canvas)
      lines_id.pop(0)
    for j in range(round(len(level1x) / 2)):
      lines_id.append(Line(canvas, level1x[j * 2], level1y[j * 2], level1x[j * 2 + 1], level1y[j * 2 + 1]))
    before_level = level

  UpdateY()

  root.after(50, UpdateUniverse)

def Collision():
  global world_x
  global world_y

  in_bounds = []
  for i in range(round(len(level1x) / 2)):
    if_colliding = False
    # seeing if circle is in-bounds of current platform.
    x2 = -world_x + 40
    x1 = -world_x + 10
    y1 = -world_y + 435
    y2 = -world_y + 465

    av_pl_x = (x1 + x2) / 2
    av_pl_y = (y1 + y2) / 2
    av_plat_x =(level1x[i * 2] + level1x[(i * 2) + 1]) / 2
    av_plat_y =(level1y[i * 2] + level1y[(i * 2) + 1]) / 2

    if x2 < level1x[i * 2] or x1 > level1x[(i * 2) + 1] or y2 < level1y[i * 2] or y1 > level1y[(i * 2) + 1]:
      pass
    else:
      if av_pl_x < av_plat_x:
        in_bounds.append(1)
      if av_pl_x > av_plat_x:
        in_bounds.append(2)
      if av_pl_y < av_plat_y:
        in_bounds.append(3)
      if av_pl_y > av_plat_y:
        in_bounds.append(4)
      in_bounds.append(i * 2)
    #print(in_bounds)
  return in_bounds

def UpdateY():
  global gravity
  global jump
  global world_y
  global world_x

  collision_walls = Collision()
  if 4 in collision_walls:
    gravity = 0
    jump = 0
    #print(world_y)
    world_y = -(level1y[collision_walls[-1] * 2] - 465)
    #print(world_y)
    for j in range(round(len(level1x) / 2)):
      lines_id[j].setcoordsy(canvas, 0, world_y + level1y[j * 2], 0, world_y + level1y[(j * 2) + 1])
  elif 3 in collision_walls:
    jump = 0
    world_y -= 1
    gravity = 1
  else:
    world_y += -gravity + jump
    gravity += 1
  print(jump)
  for i in range(round(len(level1x) / 2)):
    lines_id[i].update(canvas, 0, -gravity + jump)

# the Jump() function below is just for the event.
def Jump(event):
  global jump

  if 4 or 3 in collision_walls:
    jump = 10
    for i in range(round(len(level1x) / 2)):
      lines_id[i].update(canvas, 0, 10)
def MoveL(event):
  global world_x

  collision_walls = Collision()

  if 4 or 3 in collision_walls:
    world_x += 5
    for i in range(round(len(level1x) / 2)):
      lines_id[i].update(canvas, 5, 0)

def MoveR(event):
  global world_x

  collision_walls = Collision()

  if 4 or 3 in collision_walls:
    world_x -= 5
    for i in range(round(len(level1x) / 2)):
      lines_id[i].update(canvas, -5, 0)

canvas.focus_set()
canvas.bind("w", Jump)
canvas.bind("a", MoveL)
canvas.bind("d", MoveR)
root.after(50, UpdateUniverse)
root.mainloop()
