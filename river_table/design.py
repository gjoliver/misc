from matplotlib import pyplot as plt
import numpy

HEIGHT = 36.0  # inches
THICKNESS = 1.3  # inches
BLOCK_WIDTH = 1.5  # inches
# This is a candidate design that looks pretty good.
PICKED_DESIGN = [0.1, 0.1, 0.1, 0.3, 0.3, 0.1, 0.1, 0.7, 0.5, 0.1,
                 0.5, 0.1, 0.1, 0.1, 0.5, 0.5, 0.1, 0.3, 0.7, 0.1,
                 0.7, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.1, 0.1, 0.3,
                 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.1, 0.1, 0.3, 0.1,
                 0.1, 0.1, 0.1, 0.1, 0.1, 0.7, 0.3, 0.5, 0.1, 0.1,
                 0.3, 0.1, 0.1, 0.7, 0.1, 0.3]

image = plt.imread('./sound_wav_small.png')
wav = image[:, :, 0]

if True:  # Change this line to generate a random design.
  bars = PICKED_DESIGN
else:
  bars = numpy.array([0.1] * 36 + [0.3] * 8 + [0.5] * 7 + [0.7] * 5)
  numpy.random.shuffle(bars)

table = numpy.tile(bars, [25, 1])
half_bar_size = [12] * 56

# Build sound wave river.
total_river_blocks = 0
for i in range(25):
  for j in range(56):
    if wav[i, j] == 0.0:
      table[i, j] = 0.0
      total_river_blocks += 1

      # Update half block size.
      if i < 12:
        half_bar_size[j] = min(half_bar_size[j], i)

# Now, let's caculate the volume of the river.
vol_per_block = THICKNESS * (HEIGHT / 25.0) * BLOCK_WIDTH
total_vol_liters = vol_per_block * total_river_blocks * 0.0163871

print 'Total river volume: ', total_vol_liters

NAMES = ['MP', 'CR', 'MH', 'WN']
def FloatToName(f):
  return NAMES[int(f * 10 / 2)]

pivot_table = dict([(n, {}) for n in NAMES])
print '#, Type (MP: Maple, CR: Cherry, MH: Mahogany, WN: Walnet), Half Length (inches)'
for i in range(56):
  name = FloatToName(bars[i])
  length = half_bar_size[i] * 1.4
  pivot_table[name][str(length)] = pivot_table[name].get(str(length), 0) + 1

  print i + 1, name, length

unique_lengths = []
for n in NAMES:
  unique_lengths += pivot_table[n].keys()
unique_lengths = sorted([float(l) for l in set(unique_lengths)])

print '  ',
for u in unique_lengths:
  print '%s,' % u,
print ''
for n in NAMES:
  print '%s,' % n,
  for u in unique_lengths:
    print '%s,' % pivot_table[n].get(str(u), 0),
  print ''


plt.imshow(table, aspect='auto', cmap='binary', interpolation='none',
           vmin=0.0, vmax=1.0)

plt.show()
