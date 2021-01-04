import constants as c
import math

class AObject(object):
  def Next(self, canvas):
    assert False, 'Need to implement Next.'

  def IsDone(self):
    assert False, 'Need to implement IsDone.'

  def Delete(self, canvas):
    canvas.delete(self.id)


class Bullet(AObject):
  def __init__(self, canvas, x, y, slope, speed):
    self.x = x
    self.y = y
    self.slope = slope
    self.speed = speed

    self.id = canvas.create_oval(
      x - 2, y - 2, x + 2, y + 2, fill='red')

  def Next(self, canvas):
    self.x += math.cos(self.slope) * self.speed
    self.y += math.sin(self.slope) * self.speed
    canvas.coords(self.id, (self.x - 2, self.y - 2, self.x + 2, self.y + 2))

  def IsDone(self):
    return self.x < 0 or self.x > c.WIDTH or self.y < 0 or self.y > c.HEIGHT


class BadGuy(AObject):
  def __init__(self, canvas, speed):
    self.x = random.random() * c.WIDTH
    self.y = 0
    self.speed = speed

  def Next(self, canvas):
    pass

  def IsDone(self):
    return False


class Bunker(AObject):
  def __init__(self, canvas):
    self.oval_id = canvas.create_oval(c.CENTER_X - 5,
                                      c.CENTER_Y - 5,
                                      c.CENTER_X + 5,
                                      c.CENTER_Y + 5)
    self.line_id = canvas.create_line(c.CENTER_X,
                                      c.CENTER_Y,
                                      c.CENTER_X,
                                      c.CENTER_Y - c.AIM_LENGTH)

  def Next(self, canvas, slope):
    end_x = c.CENTER_X + c.AIM_LENGTH * math.cos(slope)
    end_y = c.CENTER_Y + c.AIM_LENGTH * math.sin(slope)
    canvas.coords(self.line_id, (c.CENTER_X, c.CENTER_Y, end_x, end_y))

  def IsDone(self):
    return False
