import tkinter
import random
import math

WIDTH = 1200
HEIGHT = 900

root = tkinter.Tk()
root.title('nothing')

canvas = tkinter.Canvas(root,
                        bg='black',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

pixel_size = 25
offset = 6

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
def UpdateUniverse():
  root.after(50, UpdateUniverse)



canvas.focus_set()
#canvas.bind('<Motion>',)

root.after(50, UpdateUniverse)
root.mainloop()
