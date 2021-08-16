import math
import tkinter
from tkinter import font

WIDTH = 1200
HEIGHT = 900


root = tkinter.Tk()
root.title('Conway\'s Game of Life')

canvas = tkinter.Canvas(root,
                        bg='gray50',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

pixel_size = 10

num_rows = round((HEIGHT + 10) / pixel_size)
num_cols = round(WIDTH / pixel_size)

button = False

cam_x = 0
cam_y = 0

rowname = []
for row in range(num_rows):
  columnname = []
  for col in range(num_cols):
    columnname.append({'state' = 0, 'live_count' = 0})
  rowname.append(columnname)

h = canvas.create_text(WIDTH / 2, 5, text = 's†å®t', fill = 'white', activefill = 'gray75', width = 1200)

def mouseclick(event):
  global HEIGHT
  global WIDTH
  global pixel_size
  global button
  global cam_x
  global cam_y

  if event.y < 10 and button == False:
    canvas.itemconfig(h, text = 's†øp')
    button = True
  elif event.y < 10 and button == True:
    canvas.itemconfig(h, text = 's†å®t')
    button = False

  if button == False:
    row = round(cam_y + (event.y - 10 - (event.y % pixel_size)) / pixel_size)
    col = round(cam_x + (event.x - (event.x % pixel_size)) / pixel_size)

    if rowname[row][col] == 0:
      rowname[row][col] = 1
    else:
      rowname[row][col] = 0


class cell(self, row, col, state, live_count):
  self.row = row
  self.col = col
  self.state = state
  self.live_count = live_count

  def __init__():
    return

  def cellCount():
    global num_rows
    global num_cols
    global cam_x
    global cam_y

    for i in range(3):
      for j in range(3):
        if i + self.row j + self.col self.state == 1:# need a way to keep track of the cells around it.
          self.livecount + 1

    self.live_count - self.state

  def rules(count):
    # dead rule
    if self.state == 0 and self.live_count == 3:
      self.state = 1

    # live rule
    elif self.state == 1 and self.live_count < 2 or self.live_count > 3:
      self.state = 0

def UpdateUniverse():
  root.after(50, UpdateUniverse)



canvas.focus_set()
canvas.bind('<ButtonPress-1>', mouseclick)

root.after(50, UpdateUniverse)
root.mainloop()
