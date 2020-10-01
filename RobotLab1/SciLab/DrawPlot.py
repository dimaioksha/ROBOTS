import matplotlib.pyplot as plt

def ReadFile(name):
	f = open(name, 'r')
	time = []
	values = []
	for line in f:
		v = [float(i) for i in line.split()]
		values.append(v[0])
		time.append(v[1])
	return [values, time]

data = ReadFile('..\\Data\\Tm.txt')

plt.plot(data[1], data[0], '-r')

plt.minorticks_on()
plt.grid(which="major", color="k", linewidth=0.5)
plt.grid(which="minor", color="k", linestyle=":", linewidth=0.5)

plt.show()
