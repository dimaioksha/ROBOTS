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

data = ReadFile('..\\Data\\Mst.txt')

plt.plot(data[1], data[0], '-r')

plt.show()
