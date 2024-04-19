import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(0, 2*numpy.pi, 100)

while True:
    for a in numpy.linspace(0, 2*numpy.pi, 100):
        y = numpy.sin(x+a)
        plt.cla()
        plt.grid()
        plt.plot(x, y)
        plt.pause(0.00001)
