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
        if ret[1][-1] > 0.5:
            break;
    return ret

colors = ['r', 'g', '--b']

for idx in range(-10, -1, 2):
    data     = ReadFile('../Data/log' + str(idx * 10) + '.txt')
    theta    = ReadFile('../Sim/Theta_simply_Sim' + str(idx * 10) + '.txt')
    thetaDot = ReadFile('../Sim/ThetaDot_simply_Sim' + str(idx * 10) + '.txt')

    data[0] = [i * 0.017453 for i in data[0]]


    plt.plot(theta[1], theta[0], colors[0], alpha=1.0, linewidth=1, label=('θ(t)' if idx == -10 else ''))
    plt.plot(thetaDot[1], thetaDot[0], colors[1], alpha=0.9, linewidth=1, label=('ω(t)' if idx == -10 else ''))
    plt.plot(data[1], data[0], colors[2], alpha=0.8, linewidth=1, label=('θ(t) - measured' if idx == -10 else ''))

plt.minorticks_on()
plt.grid(which="major", color="k", linewidth=0.5, alpha=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5, alpha=0.5)
plt.legend()
plt.show()
