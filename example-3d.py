import numpy
import matplotlib.pyplot as plt

t = numpy.linspace(0, 2*numpy.pi, 100)
zero = [0]*100

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
while True:
    for a in numpy.linspace(0, 2*numpy.pi, 70):
        wave = 5*numpy.sin(t+a)
        ax.clear()
        ax.plot(t, wave, zero, color="blue")
        ax.plot(t, zero, wave, color="green")
        ax.scatter(0, 0, wave[0], color="blue")

        ax.plot([numpy.pi/2, numpy.pi/2], [0, 5*numpy.sin(a+numpy.pi/2)], [0, 0], color="blue")
        ax.plot([numpy.pi/2, numpy.pi/2], [0, 0], [0, 5*numpy.sin(a+numpy.pi/2)], color="green")
        ax.plot([3*numpy.pi/2, 3*numpy.pi/2], [0, 5*numpy.sin(a+3*numpy.pi/2)], [0, 0], color="blue")
        ax.plot([3*numpy.pi/2, 3*numpy.pi/2], [0,0], [0, 5*numpy.sin(a+3*numpy.pi/2)], color="green")

        plt.pause(0.00001)
plt.show()