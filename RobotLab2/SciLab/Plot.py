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
        if time[-1] > 0.5:
            break;
    return [values, time]

colors = ['r', 'g', '--b']

for idx in range(1, 10, 2):
    data = ReadFile('../Data/log' + str(idx * 10) + '.txt')
    theta = ReadFile('../Sim/ThetaSim' + str(idx * 10) + '.txt')
    thetaDot = ReadFile('../Sim/ThetaDotSim' + str(idx * 10) + '.txt')

    data[0] = [i * 0.017453 for i in data[0]]


    plt.plot(theta[1], theta[0], colors[0], alpha=1.0, linewidth=1, label=('θ(t)' if idx == 1 else ''))
    plt.plot(thetaDot[1], thetaDot[0], colors[1], alpha=0.9, linewidth=1, label=('ω(t)' if idx == 1 else ''))
    plt.plot(data[1], data[0], colors[2], alpha=0.8, linewidth=1, label=('θ(t) - measured' if idx == 1 else ''))

plt.minorticks_on()
plt.grid(which="major", color="k", linewidth=0.5, alpha=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5, alpha=0.5)
plt.legend()
plt.show()
