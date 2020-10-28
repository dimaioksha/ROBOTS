import matplotlib.pyplot as plt

plt.style.use('fast')

def ReadFile(name, cols=2):
    f = open(name, 'r')
    ret = []
    for i in range(cols):
        ret.append([])
    for line in f:
        v = [float(i) for i in line.split()]
        for i in range(cols):
            ret[i].append(v[i])
    return ret

colors = ['r', '--b']

data = ReadFile('../Data/FwElectrical.txt', 2)
Wnls = ReadFile('../Data/FwWnls.txt', 1)[0]

Wnls.reverse()
ke = 0.4872294

xs = [ Wnls[0], Wnls[-1] ]
ys = [ ke * xs[0], ke * xs[-1] ]
plt.plot(xs, ys, colors[0], alpha=1.0, linewidth=1, label='ε(ω) - approximation')
plt.plot(Wnls, data[0], colors[1], alpha=0.8, linewidth=1, label='ε(ω)')

plt.minorticks_on()

plt.grid(which="major", color="k", linewidth=0.5, alpha=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5, alpha=0.5)
plt.legend()

plt.show()
