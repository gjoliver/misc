import tkinter
import random
import math
import tkinter.font as tkFont

WIDTH = 1200
HEIGHT = 900

root = tkinter.Tk()
root.title('nothing')

canvas = tkinter.Canvas(root,
                        bg='dark slate gray',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

pixel_size = 25

font = tkFont.Font(family='Helvetica', size=20)

mousex = 0
mousey = 0


color_rect_size = 8

color = 50

gradient_id = []
for gradient in range(100):
  id = canvas.create_rectangle(WIDTH - 145, 50 + (gradient * color_rect_size),
                               WIDTH - 5, 50 + color_rect_size + (gradient * color_rect_size),
                               fill = "gray" + str(gradient),
                               outline = 'turquoise',
                               width = 2)
  gradient_id.append(id)

recent_cols = [35, 15, 10, 5, 50]
recent_cols_boxes = []

for recent in range(5):
  id = canvas.create_rectangle(WIDTH - 260,
                              50 + (60 * recent),
                              WIDTH - 155,
                              50 + ((recent + 1) * 60),
                              fill = 'gray' + str(recent_cols[recent]))
  recent_cols_boxes.append(id)

recent_cols_text = []

for recent_text in range(5):
  id = canvas.create_text(WIDTH - 280,
                          80 + (60 * recent_text),
                          font = font,
                          fill = 'white',
                          text = str(recent_cols[recent_text]))
  recent_cols_text.append(id)

offset = 6

rows = int(HEIGHT / pixel_size)

cols = int((WIDTH - 20) / pixel_size)

rowname = []
for row in range(int(HEIGHT / pixel_size)):
  colname = []
  for col in range(int((WIDTH - 20) / pixel_size)):
    #+offset and -offset for octagon-shaped polygons
    id = canvas.create_polygon(row * pixel_size, col * pixel_size + offset,
                               row * pixel_size, (col + 1) * pixel_size - offset,
                               row * pixel_size + offset, (col + 1) * pixel_size,
                               (row + 1) * pixel_size - offset, (col + 1) * pixel_size,
                               (row + 1) * pixel_size, (col + 1) * pixel_size - offset,
                               (row + 1) * pixel_size, col * pixel_size + offset,
                               (row + 1) * pixel_size - offset, col * pixel_size,
                               row * pixel_size + offset, col * pixel_size,
                               outline = 'turquoise',
                               fill = 'white')

    colname.append(id)
  rowname.append(colname)

erase_rect_id = canvas.create_rectangle(910, 400, WIDTH - 155, 430, fill = 'turquoise')

erase_all_id = canvas.create_rectangle(910, 390, WIDTH - 155, 360, fill = 'turquoise')

erase = 0

erase_all = 0

time = 0
def UpdateUniverse():
  global time

  Clear()

  flicker_speed = 4
  canvas.itemconfig(gradient_id[color], outline = 'gray' + str(round(100 * ((1 + math.sin(math.radians(time * flicker_speed % 360))) / 2))))
  root.after(50, UpdateUniverse)

col_display_id = canvas.create_text(975, HEIGHT/2, font = font, fill = 'white', text = 'gray_50')

erase_display_id = canvas.create_text(975, 415, font = font, fill = 'white', text = 'Not erasing')

erase_all_display_id =canvas.create_text(975, 375, font = font, fill = 'white', text = 'Erase all')

def Clear():
  global color
  global time
  global erase
  global erase_all
  global mousex
  global mousey

  erase_all_text = ''
  erase_text = ''

  time += 1

  canvas.itemconfig(col_display_id, text = color)

  if erase == 0:
    erase_text = 'Not erasing'
  else:
    erase_text = 'Erasing'

  if erase_all == 0:
    erase_all_text = 'Erase all'
  else:
    erase_all_text = 'Are you sure?'

  canvas.itemconfig(erase_display_id, text = erase_text)

  canvas.itemconfig(erase_all_display_id, text = erase_all_text)

  # highlights selected color box
  for resetbox in range(100):
    canvas.itemconfig(gradient_id[resetbox], outline = 'turquoise', width = 2)
  canvas.itemconfig(gradient_id[color], width = 5)

  if mousex > WIDTH - 145 and mousey > 50 and mousex < WIDTH - 5 and mousey < 842:
    realcolor = mousey - 50
    canvas.itemconfig(col_display_id, text = round((realcolor - realcolor % 8) / 8))

  else:
    canvas.itemconfig(col_display_id, text = color)


def Click(x,y):
  global color
  global erase

  pixel_x = (x - (x % pixel_size)) / pixel_size
  pixel_y = (y - (y % pixel_size)) / pixel_size
  if erase == 0:
    canvas.itemconfig(rowname[round(pixel_x)][round(pixel_y)], fill = 'gray' + str(color))
  if erase == 1:
    canvas.itemconfig(rowname[round(pixel_x)][round(pixel_y)], fill = 'gray100')

def Change_Color(x, y):
  global color

  whichboxclicked = 0
  if x < WIDTH - 5 and x > WIDTH - 145 and y < 850 and y > 50:
    cryr = y - 50
    color = round((cryr - cryr % 8) / 8)
    whichboxclicked = 6
  if x < WIDTH - 155 and x > WIDTH - 260 and y < 350 and y > 50:
    wryr = y - 50
    whichboxclicked = round((wryr - wryr % 60) / 60)
  Recent_Switcher(color, whichboxclicked)

will_color = 0

def Recent_Switcher(color1, boxclicked):
  global color

  if boxclicked < 5:
    ghost_list = []
    for ghost_list_apendees in range(5):
      ghost_list.append(recent_cols[ghost_list_apendees])
    for recent_switches in range(boxclicked):
      recent_cols[recent_switches + 1] = ghost_list[recent_switches]
    recent_cols[0] = ghost_list[boxclicked]
    color = recent_cols[0]
  elif boxclicked == 6:
    # 6 means new color introduced
    recent_cols[4] = recent_cols[3]
    recent_cols[3] = recent_cols[2]
    recent_cols[2] = recent_cols[1]
    recent_cols[1] = recent_cols[0]
    recent_cols[0] = color1
  for change_cols in range(5):
    canvas.itemconfig(recent_cols_boxes[change_cols], fill = 'gray' + str(recent_cols[change_cols]))
    canvas.itemconfig(recent_cols_text[change_cols], text = str(recent_cols[change_cols]))

def Erase_All():
  global rows
  global cols

  for erase_all_rows in range(rows):
    for erase_all_cols in range(cols):
      canvas.itemconfig(rowname[erase_all_rows][erase_all_cols], fill = 'white')

# last functions
def IsDown(event):
  global will_color
  global erase
  global erase_all

  if event.x < 900:
    will_color = 1
    Click(event.x, event.y)

  Change_Color(event.x, event.y)

  if event.x > 910 and event.y > 400 and event.x < WIDTH - 155 and event.y < 430:
    if erase == 0:
      erase = 1
    else:
      erase = 0

  if erase_all == 1:
    Erase_All()
#do not write on this line
def IsMove(event):
  global will_color
  global erase_all
  global col_display_id
  global color
  global mousey
  global mousex

  mousey = event.y
  mousex = event.x

  if will_color == 1:
    Click(event.x, event.y)

  if event.x > 910 and event.y > 360 and event.x < WIDTH - 155 and event.y < 390:
    erase_all = 1
  else:
    erase_all = 0
#do not write on this line
def  IsUp(event, ):
  global will_color

  will_color = 0
#do not write on this line
#do not write on this line
canvas.focus_set()
canvas.bind('<ButtonPress-1>', IsDown)
canvas.bind('<Motion>', IsMove)
canvas.bind('<ButtonRelease-1>', IsUp)
root.after(50, UpdateUniverse)
root.mainloop()
B
