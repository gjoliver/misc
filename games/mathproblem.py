import math
import tkinter
from tkinter import font

WIDTH = 1200
HEIGHT = 900


root = tkinter.Tk()
root.title('math problem')

canvas = tkinter.Canvas(root,
                        bg = 'black',
                        height = HEIGHT,
                        width = WIDTH)
canvas.pack()


canvas.create_oval(599, 449, 601, 451, fill = 'white', width = 0)

degreelines = []
for h in range(4):
  id = canvas.create_line(600,
                          450,
                          600 + round(math.sin(math.radians(h * 90))) * 600,
                          450 + round(math.cos(math.radians(h * 90))) * 600,
                          fill = 'black')

  degreelines.append(id)

text1 = canvas.create_text(1100, 15, text = '(there are 5 red lines because \n this isn\'t a closed shape.)', fill = 'white', font = 'bold')

text2 = canvas.create_text(1100, 15, text = '(there are 5 red lines because \n this isn\'t a closed shape.)', fill = 'black')

number = canvas.create_text(30, 12, text = '2', fill = 'gray75', font = ("Courier", 10))

slider = canvas.create_oval(20, 22, 40, 2, outline = 'white', activeoutline = 'gray')

segments = 2.5

divisor = 2

lines = []

prooflines = []

zoom = 5

down = False

for a in range(360):
  id = canvas.create_rectangle(0, 0, 1, 1, width = 0, fill = 'white')

  lines.append(id)

for b in range(4):
  canvas.itemconfig(lines[b * 90], fill = 'orange')

def buttondown_press(event):
  global segments
  global down
  global divisor
  global zoom

  y = event.y

  if event.y > 60:
    y = 60
  if event.y < 10:
    y = 10

  if event.x > 24 and event.x < 31 and event.y > 9 and event.y < 51:
    down = True

  if down:

    for c in range(len(prooflines)):
      canvas.delete(prooflines[0])
      del prooflines[0]
    segments = y - 20

    canvas.coords(slider, 20, y + 10, 40, y - 10)
    canvas.coords(number, 30, y)
    canvas.itemconfig(number, text = segments)

    for d in range(360):
      x = 600
      y = 450
      for e in range(segments):
        length = (50 - e) / divisor / (e + 1)

        if e % 2 == 0:
          angle = d * -1 / segments
        else:
          angle = d / segments

        x += length * math.sin(math.radians(d + angle)) * zoom
        y += length * math.cos(math.radians(d + angle)) * zoom

      canvas.coords(lines[d], x, y, x + 1, y + 1)

    for f in range(17):
      x2 = 600 + math.sin(math.radians(f * 360 / 16))
      y2 = 450 + math.cos(math.radians(f * 360 / 16))
      nx2 = x2
      ny2 = y2
      for g in range(segments):
        length2 = (50 - g) / divisor / (g + 1)

        if g % 2 == 0:
          angle2 = f * -1 / segments
        else:
          angle2 = f / segments

        if f % 4 == 0:
          color = 'red'
        elif f % 2 == 0:
          color = 'pink3'
        else:
          color = 'gray50'

        nx2 += length2 * math.sin(math.radians((f + angle2) * 360 / 16)) * zoom
        ny2 += length2 * math.cos(math.radians((f + angle2) * 360 / 16)) * zoom

        id = canvas.create_line(x2, y2, nx2, ny2, fill = color, width = 0)
        prooflines.append(id)

        x2 = nx2
        y2 = ny2

def buttonup(event):
  global down

  if down:
    down = False

state = False

def check(event):
  global state

  if state:
    color2 = 'white'
    state = False
  else:
    color2 = 'black'
    state = True

  for j in range(4):
    canvas.itemconfig(degreelines[j], fill = color2)

def UpdateUniverse():
  pass
  #root.after(50, UpdateUniverse)

canvas.focus_set()
canvas.bind('<B1-Motion>', buttondown_press)
canvas.bind('<ButtonRelease-1>', buttonup)
canvas.bind('<c>', check)

root.after(50, UpdateUniverse)
root.mainloop()
