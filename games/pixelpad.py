import math
import random
import tkinter
from tkinter import font

WIDTH = 1200
HEIGHT = 900


shade = 0

def line(canvas):
  global shade
  count = 1
  for i in range(99):
    shade = 'gray' + str(count)
    canvas.create_rectangle(600 - (100 - 2 * count), 20, 600 - (100 - (2 * count + 1)), 25, outline = str(shade), fill = str(shade))
    count += 1

root = tkinter.Tk()
root.title('Jayden\'s Game')

canvas = tkinter.Canvas(root,
                        bg='old lace',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

line(canvas)

buttondown = False

color = 'gray50'

oval_id = canvas.create_oval(600 - 5, 17.5, 600 + 5, 27.5, outline = 'gray50', fill = 'gray50')
canvas.lift(oval_id)

def UpdateUniverse():
  root.after(50, UpdateUniverse)

def dotdown(event):
  global buttondown

  if event.y < 26 and event.y > 19 and event.x < 701 and event.x > 499:
    buttondown = True

def dotmove(event):
  global buttondown
  global color

  if buttondown == True:
    realx = event.x
    if event.x > 700:
      realx = 700
    if event.x < 500:
      realx = 500
    canvas.coords(oval_id, realx - 5, 17.5, realx + 5, 27.5)
    color = "gray" + str(round((realx - 500) / 2))
    canvas.itemconfig(oval_id, outline = str(color), fill=str(color))

pixel_size = 25


num_rows = round((HEIGHT - 50) / pixel_size)
num_cols = round(WIDTH / pixel_size)

rowname = []
for row in range(num_rows):
  columnname = []
  for col in range(num_cols):
    id = canvas.create_rectangle(col * pixel_size,
                                 (row + 2) * pixel_size,
                                 col * pixel_size + pixel_size,
                                 (row + 2) * pixel_size + pixel_size,
                                 outline = 'old lace',
                                 fill = 'white')

    columnname.append(id)
  rowname.append(columnname)


def draw(event):
  global color
  global pixel_size
  eventrow = round((event.x - event.x % pixel_size) / pixel_size)
  eventcol = round((event.y - 50 - event.y % pixel_size) / pixel_size)
  print(eventrow, eventcol, len(rowname), len(rowname[eventrow]))
  # Here we just update color on the corresponding "pixel"
  canvas.itemconfig(rowname[eventcol][eventrow], fill = str(color))


def dotup(event):
  global buttondown
  buttondown = False

  if event.y > 50:
    draw(event)


canvas.focus_set()
canvas.bind('<Motion>', dotmove)
canvas.bind('<ButtonPress-1>', dotdown)
canvas.bind('<ButtonRelease-1>', dotup)

root.after(50, UpdateUniverse)
root.mainloop()
