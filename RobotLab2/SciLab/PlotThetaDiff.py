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
        if ret[1][-1] > 0.25:
            break;
    return ret

colors = ['r', 'g', '--b']

for idx in range(-10, -1, 2):
    simple = ReadFile('../Sim/Theta_simply_Sim' + str(idx * 10) + '.txt')
    full   = ReadFile('../Sim/ThetaSim' + str(idx * 10) + '.txt')
    data   = ReadFile('../Data/log' + str(idx * 10) + '.txt')
    
    data[0] = [ i * 0.017453292 for i in data[0]]

    plt.plot(full[1], full[0], colors[0], alpha=0.9, linewidth=1, label=('θ(t) - full' if idx == -10 else ''))
    plt.plot(simple[1], simple[0], colors[1], alpha=0.9, linewidth=1, label=('θ(t) - simple' if idx == -10 else ''))
    plt.plot(data[1], data[0], colors[2], alpha=0.9, linewidth=1, label=('θ(t) - data' if idx == -10 else ''))

plt.minorticks_on()
plt.grid(which="major", color="k", linewidth=0.5, alpha=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5, alpha=0.5)
plt.legend()
plt.show()
