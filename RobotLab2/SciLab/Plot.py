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

colors = ['r', '--b']

for idx in range(-10, 0):
    data = ReadFile('../Data/log' + str(idx * 10) + '.txt')
    sim = ReadFile('../Sim/Sim' + str(idx * 10) + '.txt')

    data[0] = [i * 0.017453 for i in data[0]]


    plt.plot(sim[1], sim[0], colors[0], alpha=1.0, linewidth=1)
    plt.plot(data[1], data[0], colors[1], alpha=0.8, linewidth=1)

plt.minorticks_on()
plt.grid(which="major", color="k", linewidth=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5)

plt.show()
