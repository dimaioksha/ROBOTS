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
        if ret[1][-1] > 0.05:
            break;
    return ret

colors = ['r', 'g', '--b']

for idx in range(-10, -1, 2):
    simple = ReadFile('../Sim/ThetaDot_simply_Sim' + str(idx * 10) + '.txt')
    full   = ReadFile('../Sim/ThetaDotSim' + str(idx * 10) + '.txt')

    plt.plot(full[1], full[0], colors[0], alpha=0.9, linewidth=1, label=('ω(t) - full' if idx == -10 else ''))
    plt.plot(simple[1], simple[0], colors[1], alpha=0.9, linewidth=1, label=('ω(t) - simple' if idx == -10 else ''))

plt.minorticks_on()
plt.grid(which="major", color="k", linewidth=0.5, alpha=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5, alpha=0.5)
plt.legend()
plt.show()
