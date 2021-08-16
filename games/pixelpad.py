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

canvas.create_text(787.5, 10, text = 'recent colors')

canvas.create_rectangle(375, 20, 425, 40, activefill = 'firebrick1', fill = 'gray75')

canvas.create_text(400, 10, text = 'erase all')

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

buttondown = False

eraseall = False

recentupdate = False

pressed = False

rect_num = 0

color = 'gray50'

# slider dot
oval_id = canvas.create_oval(600 - 5, 17.5, 600 + 5, 27.5, outline = 'gray50', fill = 'gray50')
canvas.lift(oval_id)

def UpdateUniverse():
  root.after(50, UpdateUniverse)

# when the mouse is down
def dotdown(event):
  global buttondown
  global recentupdate
  global eraseall
  global pressed
  global HEIGHT
  global WIDTH
  global rect_num

  # if the mouse is in the screen
  if event.y < HEIGHT and event.y > 0 and event.x > 0 and event.x < WIDTH:
    # if the mouse is clicking on the recent colors
    if event.y > 4 and event.y < 31 and event.x > 724 and event.x < 876:
      recentupdate = True

      rect_num = round((event.x - event.x % 25 - 725) / 25)

    if event.y > 19 and event.y < 41 and event.x > 374 and event.x < 426:
      eraseall = True

    if event.y < 26 and event.y > 19 and event.x < 701 and event.x > 499:
      buttondown = True

    if event.y > 50:
      pressed = True

def dotmove(event):
  global buttondown
  global color

# the color changer
  if buttondown == True:
    realx = event.x
    if event.x > 700:
      realx = 700
    if event.x < 500:
      realx = 500
    canvas.coords(oval_id, realx - 5, 17.5, realx + 5, 27.5)
    color = "gray" + str(round((realx - 500) / 2))
    canvas.itemconfig(oval_id, outline = str(color), fill=str(color))
# the drawer
  if event.y > 50 and buttondown == False and pressed == True:
     draw(event)


def draw(event):
  global color
  global pixel_size
  global num_rows
  global num_cols
  eventrow = round((event.x - event.x % pixel_size) / pixel_size)
  eventcol = round((event.y - 50 - event.y % pixel_size) / pixel_size)

  # Here we just update color on the corresponding "pixel"
  canvas.itemconfig(rowname[eventcol][eventrow], fill = str(color))


def erase():
  global eraseall
  if eraseall == True:
    for a in range(num_rows):
      for b in range(num_cols):
        canvas.itemconfig(rowname[a][b], fill = 'white')

recent_colors = ['gray50', 'gray50', 'gray50', 'gray50', 'gray50']

def dotup(event):
  global buttondown
  global eraseall
  global pressed
  global recentupdate
  global rect_num
  global color


  if eraseall == True:
    erase()
    eraseall = False

  if buttondown == True:
    recent_colors[4] = recent_colors[3]
    recent_colors[3] = recent_colors[2]
    recent_colors[2] = recent_colors[1]
    recent_colors[1] = recent_colors[0]
    recent_colors[0] = color

  if buttondown == True:
    drawRecentColors(rect_num, color, recentupdate)

  if event.y > 50 and not buttondown == True:
    draw(event)

  buttondown = False

  pressed = False

recent_color_rect = []
offset = 0
for thing in range(5):
  thing = round(offset / 25)
  id = canvas.create_rectangle(725 + offset, 20, 750 + offset, 45,
                               fill = recent_colors[thing],
                               outline = recent_colors[thing])
  offset += 25
  recent_color_rect.append(id)


def drawRecentColors(rect_num, color, recent_update):
  for v in range(5):
    canvas.itemconfig(recent_color_rect[v], fill = recent_colors[v], outline = recent_colors[v])

  if recentupdate == True:
    print(rect_num)
    canvas.itemconfig(oval_id, fill = recent_colors[rect_num], outline = recent_colors[rect_num])
    color = recent_colors[rect_num]
    recentupdate = False

canvas.focus_set()
canvas.bind('<Motion>', dotmove)
canvas.bind('<ButtonPress-1>', dotdown)
canvas.bind('<ButtonRelease-1>', dotup)

root.after(50, UpdateUniverse)
root.mainloop()
