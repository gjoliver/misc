from matplotlib import pyplot as plt
import numpy

HEIGHT = 36.0  # inches
THICKNESS = 1.3  # inches
BLOCK_WIDTH = 1.5  # inches

image = plt.imread('/Users/jungong/Downloads/sound_wav_small.png')
wav = image[:, :, 0]

bars = numpy.array([0.1] * 36 + [0.3] * 8 + [0.5] * 7 + [0.7] * 5)
numpy.random.shuffle(bars)

table = numpy.tile(bars, [25, 1])

# Build sound wave river.
total_river_blocks = 0
for i in range(25):
  for j in range(56):
    if wav[i, j] == 0.0:
      table[i, j] = 0.0
      total_river_blocks += 1

# Now, let's caculate the volume of the river.
vol_per_block = THICKNESS * (HEIGHT / 25.0) * BLOCK_WIDTH
total_vol_liters = vol_per_block * total_river_blocks * 0.0163871

print 'Total river volume: ', total_vol_liters

plt.imshow(table, aspect='auto', cmap='binary', interpolation='none',
           vmin=0.0, vmax=1.0)

plt.show()
