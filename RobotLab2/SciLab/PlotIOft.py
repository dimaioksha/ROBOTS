import matplotlib.pyplot as plt
import numpy as np

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

colors = ['r', 'g', '--b']

R  = 8.4928817
J  = 0.0024376
Km = 0.4872294

electrical = ReadFile('../Data/RvElectrical.txt')

for idx in range(10):
    
    U = electrical[0][idx]
    time = np.linspace(0.0, 0.5, 100);
    data = U * np.exp(-(Km * Km * time) / (J * R)) / R

    plt.plot(time, data, 'r', alpha=0.8, linewidth=1, label=('I(t)' if idx == 0 else ''))

plt.minorticks_on()
plt.grid(which="major", color="k", linewidth=0.5, alpha=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5, alpha=0.5)
plt.legend()
plt.show()
