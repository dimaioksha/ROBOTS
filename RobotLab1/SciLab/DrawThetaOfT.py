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

for idx in range(-100, -19, 20):
	sim = ReadFile('..\\Data\\Sim' + str(idx) + '.txt')
	data = ReadFile('..\\Data\\log' + str(idx) + '.txt')
	model = ReadFile('..\\Data\\Model' + str(idx) + '.txt')

	data[0] = [i * 0.017453 for i in data[0]]
	data[1] = [i / 1000 for i in data[1]]

	plt.plot(data[1], data[0], '-.b', alpha=0.5, linewidth=2)
	plt.plot(model[1], model[0], ':g', alpha=0.8, linewidth=4)
	plt.plot(sim[1], sim[0], '--r')

plt.show()
