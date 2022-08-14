import math
import numpy as np
import tkinter
import time

WIDTH = 1200
HEIGHT = 900
NUM_WHEELS = 20
DOWN_SPEED = 0.5
TAIL_START_Y = 200


class Line(object):
  center_x = 600
  center_y = 250

  def __init__(self, x0, y0, x1, y1, id=None, color='red'):
    self.x0 = x0
    self.y0 = y0
    self.x1 = x1
    self.y1 = y1

    self.id = id
    self.color = color

  def create(self, canvas):
    self.id = canvas.create_line(
      self.center_x + self.x0,
      self.center_y + self.y0,
      self.center_x + self.x1,
      self.center_y + self.y1,
      fill=self.color)

  def update(self ,canvas):
    canvas.coords(
      self.id,
      self.center_x + self.x0,
      self.center_y + self.y0,
      self.center_x + self.x1,
      self.center_y + self.y1)
    canvas.itemconfig(self.id, fill=self.color)

  def destruct(self, canvas):
    canvas.delete(self.id)

root = tkinter.Tk()
root.title('test')

canvas = tkinter.Canvas(root,
                        bg='dark slate gray',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

RADIAN = 2 * math.pi

time = 0

#t = np.arange(0, 1.0, step=0.1)
#x = np.sin(2*np.pi*t)
x = []
for l in range(round(NUM_WHEELS / 2) + 1):
  x.append(l / 10)

for m in range(round(NUM_WHEELS / 2)):
  x.append(((NUM_WHEELS / 2) - m) / 10)


def FourierTransform(x):
  x = np.asarray(x, dtype=float)
  N = x.shape[0]
  n = np.arange(N)
  k = n.reshape((N, 1))
  M = np.exp(-2j * np.pi * k * n / N)
  return np.dot(M, x)

fourier_result = FourierTransform(x)

length = np.absolute(fourier_result)[1:NUM_WHEELS + 1] * 5
offset = np.angle(fourier_result)[1:NUM_WHEELS + 1]
rotation_speed = [k + 1 for k in range(NUM_WHEELS)]

print(length)
print(offset)

lines = [Line(0, 0, 0, 0) for i in range(NUM_WHEELS)]
for l in lines: l.create(canvas)

tail = []
proj_line = Line(0, 0, 0, 0, color='green')
proj_line.create(canvas)

paused = False

def UpdateUniverse():
  Change()

  root.after(10, UpdateUniverse)


def Pause(event):
  global paused
  paused = not paused


def Change():
  global time
  global paused

  if paused:
    return

  time += 5

  before_x = 0
  before_y = 0
  for i in range(NUM_WHEELS):
    l = lines[i]

    l.x0 = before_x
    l.y0 = before_y

    rotation = (rotation_speed[i] * time / 360) + offset[i]
    offset_x = math.sin(rotation) * length[i]
    offset_y = math.cos(rotation) * length[i]

    l.x1 = l.x0 + offset_x
    l.y1 = l.y0 + offset_y

    l.update(canvas)

    before_x = l.x1
    before_y = l.y1

  # Update projection line.
  proj_line.x0 = before_x
  proj_line.y0 = before_y
  proj_line.x1 = before_x
  proj_line.y1 = TAIL_START_Y
  proj_line.update(canvas)

  # Now move all the tail segments down.
  for s in tail:
    s.y0 += DOWN_SPEED
    s.y1 += DOWN_SPEED
    s.update(canvas)

  # Add a tail segment.
  try:
    last_tail = tail[-1]
    starting_tail_x = tail[-1].x1
    starting_tail_y = tail[-1].y1
  except Exception:
    starting_tail_x = before_x
    starting_tail_y = TAIL_START_Y

  new_tail_segment = Line(starting_tail_x,
                          starting_tail_y,
                          before_x,
                          TAIL_START_Y,
                          color='green')
  new_tail_segment.create(canvas)
  tail.append(new_tail_segment)

  # Delete expired tail.
  if len(tail) > 500:
    tail[0].destruct(canvas)
    del tail[0]


canvas.focus_set()
canvas.bind('p', Pause)
root.after(10, UpdateUniverse)
root.mainloop()
