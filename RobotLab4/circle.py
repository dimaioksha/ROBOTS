import numpy as np

ts = np.linspace(0.5, np.pi * 2 - 0.5, 40)

xs = np.cos(ts)
ys = np.sin(ts)

f = open('./pts.txt', 'w')

f.write('[')
for i in range(40):
    f.write(str(xs[i]) + ' ')
    f.write(str(ys[i]) + ';')
f.write(']')
f.close()
