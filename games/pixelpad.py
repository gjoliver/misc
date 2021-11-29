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


num_rows = round(HEIGHT - 50 / pixel_size)
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

#x is 0, y is between 1 & 16
x = 0
y = 13

oval_id2 = canvas.create_oval((y - 1) * pixel_size + 37.5 + WIDTH/2,
                              (y - 1) * pixel_size + 37.5 + HEIGHT/2,
                              WIDTH/2 - ((y - 1) * pixel_size + 12.5),
                              HEIGHT/2 - ((y - 1) *  pixel_size + 12.5),
                              outline = 'turquoise',
                              fill = None,
                              activewidth = 25,
                              width = 3)
canvas.lift(oval_id2)

def DrawDot(x,y,color11):
  canvas.itemconfig(rowname[round((HEIGHT - 100) / 2 / pixel_size + y)][round(WIDTH / 2 / pixel_size + x)], fill = color11)

while x <= y:
  print(x, y)

  DrawDot(x,y,"green")
  DrawDot(x,-y,"red")
  DrawDot(-x,y,"turquoise")
  DrawDot(-x,-y,"pink")
  DrawDot(y,x,"yellow")
  DrawDot(y,-x,"orange")
  DrawDot(-y,x,"blue")
  DrawDot(-y,-x,"purple")

  if math.pow(y,2) - (2 * x) - 1 < 0.0:
    break

  y = math.sqrt(math.pow(y,2) - (2 * x) - 1)
  x += 1

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
  global oval_id
  global color

  # if the mouse is in the screen
  if event.y < HEIGHT and event.y > 0 and event.x > 0 and event.x < WIDTH:
    # if the mouse is clicking on the recent colors
    if event.y > 19 and event.y < 46 and event.x > 724 and event.x < 876:
      recentupdate = True

      rect_num = math.floor((event.x - 725) / 25)

      color = recent_colors[rect_num]
      drawRecentColors(color, recentupdate)
      blah = int(color[4:])
      canvas.coords(oval_id, 495 + blah * 2, 17.5, 505 + blah * 2, 27.5)

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
  eventrow = round((event.x - event.x % pixel_size) / pixel_size) % num_cols
  eventcol = round((event.y - 50 - event.y % pixel_size) / pixel_size) % num_rows

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
    drawRecentColors(color, recentupdate)

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


def drawRecentColors(color, recent_update):
  global recentupdate

  if recentupdate == True:
    canvas.itemconfig(oval_id,
                      fill = color,
                      outline = color)
    templist = []
    for w in range(rect_num):
      templist.append(recent_colors[w])
    canvas.itemconfig(recent_color_rect[0], fill = recent_colors[rect_num], outline = recent_colors[rect_num])
    for x in range(rect_num - 1):
      canvas.itemconfig(recent_color_rect[x+1], fill = templist[x], outline = templist[x])
    recentupdate = False

  if recentupdate == False:
    for v in range(5):
      canvas.itemconfig(recent_color_rect[v],
                        fill = recent_colors[v],
                        outline = recent_colors[v])

canvas.focus_set()
canvas.bind('<Motion>', dotmove)
canvas.bind('<ButtonPress-1>', dotdown)
canvas.bind('<ButtonRelease-1>', dotup)

root.after(50, UpdateUniverse)
root.mainloop()
