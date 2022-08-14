import math
import tkinter
import time

WIDTH = 1200
HEIGHT = 900

root = tkinter.Tk()
root.title('sim')

canvas = tkinter.Canvas(root,
                        bg='gray25',
                        height=HEIGHT,
                        width=WIDTH)
canvas.pack()

timer = time.time()

center_dot = canvas.create_line(600,450,601,451, fill = 'red')

before_zoom = 0
now_zoom = 1

primes = [2,3,5,7]

count = 11
while len(primes) <= 100000:
  sqrt = int(math.sqrt(count))
  is_prime = True
  for k in primes:
    if count % k == 0:
      is_prime = False
      break
    if k > sqrt:
      break
  if is_prime:
    primes.append(count)
  count += 1

length = (time.time() - timer) / 60
n_length = length * 100

print(length, 'mins')
print(n_length, 'mins')

dots = []
for i in range(len(primes)):
  id = canvas.create_line(0,0,1,1, fill = 'light slate gray', width = 3)
  dots.append(id)
def Update_Universe():
  global before_zoom
  global now_zoom

  zoom()
  root.after(50, Update_Universe)
  before_zoom = now_zoom

def big(event):
  global now_zoom

  now_zoom = now_zoom * 10

def out(event):
  global now_zoom

  now_zoom = now_zoom / 10

def zoom():
  global now_zoom
  global before_zoom

  if not now_zoom == before_zoom:
    print(now_zoom)
    for i in range(len(primes)):
      primex = math.sin(primes[i]) * primes[i] * now_zoom + (WIDTH / 2)
      primey = math.cos(primes[i]) * primes[i] * now_zoom + (HEIGHT / 2)
      canvas.coords(dots[i], primex, primey, primex + 1, primey + 1)

canvas.focus_set()
canvas.bind('i', big)
canvas.bind('o', out)

root.after(50, Update_Universe)
root.mainloop()
