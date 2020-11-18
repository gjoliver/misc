from matplotlib import pyplot as plt
import numpy

image = plt.imread('/Users/jungong/Downloads/sound_wav_small.png')
wav = image[:, :, 0]

bars = numpy.array([0.1] * 36 + [0.3] * 8 + [0.5] * 7 + [0.7] * 5)
numpy.random.shuffle(bars)

table = numpy.tile(bars, [25, 1])

# Build sound wave river.
for i in range(25):
  for j in range(56):
    if wav[i, j] == 0.0:
      table[i, j] = 0.0

plt.imshow(table, aspect='auto', cmap='binary', interpolation='none',
           vmin=0.0, vmax=1.0)

plt.show()
