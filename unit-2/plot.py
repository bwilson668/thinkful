import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

mean = 0
variance = 1
sigma = np.sqrt(variance)
x = np.linspace(-3,3,100)
plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.show()
