import matplotlib.pyplot as plt

plt.style.use('fast')

def ReadFile(name):
    f = open(name, 'r')
    time = []
    values = []
    for line in f:
        v = [float(i) for i in line.split()]
        values.append(v[0])
        time.append(v[1])
    return [values, time]

colors = ['r', '--b']

data = ReadFile('../Data/FwElectrical.txt')

R = 8.4928817

xs = [ data[1][0], data[1][-1] ]
ys = [ R * xs[0], R * xs[-1] ]
plt.plot(xs, ys, colors[0], alpha=1.0, linewidth=1, label='U(I) - approximation')
plt.plot(data[1], data[0], colors[1], alpha=0.8, linewidth=1, label='U(I)')

plt.minorticks_on()
plt.grid(which="major", color="k", linewidth=0.5, alpha=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5, alpha=0.5)
plt.legend()
plt.show()
