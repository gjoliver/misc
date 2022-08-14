≈çimport tkinter
import math
import random
import time
import tkinter.font as tkFont

WIDTH = 1070
HEIGHT = 900

num_x = 4
num_y = 4

scrambled = False
percent_solved = 100

root = tkinter.Tk()
root.title('slide puzzle')

canvas = tkinter.Canvas(root,
			bg='white',
			height=HEIGHT,
			width=WIDTH)
canvas.pack()

time_lines = []
move_lines = []

time_solve = 0

move_counter = 0

font = tkFont.Font(family = 'OpenSymbol', size = 50)

canvas.create_rectangle(905, 50, 1025, 425)
canvas.create_rectangle(905, 475, 1025, 850)

canvas.create_rectangle(50, 50, 850, 850, width = 10, outline = 'dark slate gray')

slot = num_x * num_y

hex_slot = []

for m in range(num_x):
  for n in range(num_y):
    n1 = int(n * 255 / 3)
    hex1 = "{:02X}".format(n1)
    n2 = int((3 - m) * 255 / 3)
    hex2 = "{:02X}".format(n2)
    n3 = int(((m + 3 - n)/ 2) * 255 / 3)
    hex3 = "{:02X}".format(n3)

    hex_total = '#' + hex1 + hex2 + hex3
    hex_slot.append(hex_total)

timerid = canvas.create_text(450, 37.5, font = 'OpenSymbol', fill = 'steelblue3')
percentid = canvas.create_text(450, 12.5, font = 'OpenSymbol', fill = 'steelblue3', text = str(percent_solved) + '%')
move_counter_id = canvas.create_text(450, 25, font = 'OpenSymbol', fill = 'steelblue3', text = '0 moves')

x_array = []
for i in range(num_y):
  y_array = []
  for j in range(num_x):
    square_num = (j * num_y) + (i + 1)

    sqid = canvas.create_rectangle(50 + (i * 200), 50 + (j * 200), 250 + (i * 200), 250 + (j * 200), fill = hex_slot[i + j * 4], width = 0)

    if square_num != num_x * num_y:
      number = str(square_num)
    else:
      number = ''
    id = canvas.create_text(150 + (i * 200), 150 + (j * 200), text = number, font = font, fill = 'white')

    changed_tuple = [square_num, id, sqid]
    y_array.append(changed_tuple)
  x_array.append(y_array)

slot_blocker_id = canvas.create_rectangle(650, 650, 850, 850, width = 0, fill = 'white')

def UpdateUniverse():
  global num_x
  global num_y
  global percent_solved
  global scrambled
  global time_solve

  for k in range(num_x):
    for l in range(num_y):
      text_to_use = x_array[k][l][0]
      canvas.itemconfig(x_array[k][l][1], text = text_to_use)

      canvas.itemconfig(x_array[k][l][2], fill = hex_slot[text_to_use - 1])

      if x_array[k][l][0] == 0:
        canvas.coords(slot_blocker_id, 50 + (k * 200), 50 + (l * 200), 250 + (k * 200), 250 + (l * 200))
  if scrambled == True and percent_solved == 100:
    scrambled = False
    print(scrambled)
    total_time = time.time() - time_solve
    canvas.itemconfig(timerid, text = str(math.floor(total_time / 60)) + 'min(s) ' + str((round(total_time * 10) % 600) / 10) + 'secs')
  if scrambled == True:
    canvas.itemconfig(timerid, text = '•••')


def Decoder(num_x, num_y, slot):
  y = math.ceil(slot / num_x) - 1
  x = ((slot - 1) % num_y)
  return x, y

def FunctionCaller(event):
  global scrambled
  global move_counter

  if event.keysym == 'Up':
    MoveUp()
  if event.keysym == 'Down':
    MoveDown()
  if event.keysym == 'Right':
    MoveRight()
  if event.keysym == 'Left':
    MoveLeft()
  if event.keysym == 's':
    Scramble()

  Solved()
  UpdateUniverse()

  if (event.keysym == 'Up' or event.keysym == 'Down' or event.keysym == 'Left' or event.keysym == 'Right') and scrambled == True:
    move_counter += 1
    canvas.itemconfig(move_counter_id, text = str(move_counter) + ' moves')

def MoveUp():
  global num_x
  global num_y
  global slot


  if slot > num_y:
    prev_slot = slot
    slot = slot - num_x

    prev_decoded = Decoder(num_x, num_y, prev_slot)
    slot_decoded = Decoder(num_x, num_y, slot)

    x_array[prev_decoded[0]][prev_decoded[1]][0] = x_array[slot_decoded[0]][slot_decoded[1]][0]
    x_array[slot_decoded[0]][slot_decoded[1]][0] = 0

def MoveDown():
  global num_x
  global num_y
  global slot

  if slot < (num_y * (num_x - 1)) + 1:
    prev_slot = slot
    slot = slot + num_x

    prev_decoded = Decoder(num_x, num_y, prev_slot)
    slot_decoded = Decoder(num_x, num_y, slot)

    x_array[prev_decoded[0]][prev_decoded[1]][0] = x_array[slot_decoded[0]][slot_decoded[1]][0]
    x_array[slot_decoded[0]][slot_decoded[1]][0] = 0

def MoveLeft():
  global num_x
  global num_y
  global slot

  if slot % num_x != 1:
    prev_slot = slot
    slot = slot - 1

    prev_decoded = Decoder(num_x, num_y, prev_slot)
    slot_decoded = Decoder(num_x, num_y, slot)

    x_array[prev_decoded[0]][prev_decoded[1]][0] = x_array[slot_decoded[0]][slot_decoded[1]][0]
    x_array[slot_decoded[0]][slot_decoded[1]][0] = 0

def MoveRight():
  global num_x
  global num_y
  global slot

  if slot % num_x != 0:
    prev_slot = slot
    slot = slot + 1

    prev_decoded = Decoder(num_x, num_y, prev_slot)
    slot_decoded = Decoder(num_x, num_y, slot)

    x_array[prev_decoded[0]][prev_decoded[1]][0] = x_array[slot_decoded[0]][slot_decoded[1]][0]
    x_array[slot_decoded[0]][slot_decoded[1]][0] = 0

def Solved():
  global percent_solved

  percent_solved = 0
  solved_number = 0
  for p in range(num_x):
    for q in range(num_y):
      if x_array[p][q][0] == (p + 1) + q * 4:
        canvas.itemconfig(x_array[p][q][1], fill = 'green')
        solved_number += 1
      else:
        canvas.itemconfig(x_array[p][q][1], fill = 'white')
  percent_solved = round((100 * solved_number) / 15)
  canvas.itemconfig(percentid, text = str(percent_solved) + '%')

def Scramble():
  global scrambled
  global time_solve
  global move_counter

  for o in range(1000):
    rand_number = random.randint(0, 3)
    if rand_number == 0:
      MoveUp()
    elif rand_number == 1:
      MoveDown()
    elif rand_number == 2:
      MoveRight()
    else:
      MoveLeft()
  Solved()
  scrambled = True
  move_counter = 0
  time_solve = time.time()

canvas.focus_set()
canvas.bind('<Up>', FunctionCaller)
canvas.bind('<Down>',FunctionCaller)
canvas.bind('<Left>', FunctionCaller)
canvas.bind('<Right>', FunctionCaller)
canvas.bind('<s>', FunctionCaller)
root.mainloop()
