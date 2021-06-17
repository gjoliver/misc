class Car:
  CUR_LICENSE = 1

  def __init__(self):
    self.license = Car.CUR_LICENSE
    Car.CUR_LICENSE += 1



a = Car()
b = Car()
c = Car()

print(a.license)
print(b.license)
print(c.license)

a.license = 999

print(a.CUR_LICENSE)
print(b.CUR_LICENSE)
print(c.CUR_LICENSE)
