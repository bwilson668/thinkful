import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

data = np.random.normal(size=500)

plt.figure()
plt.boxplot(data)
plt.savefig('boxplot.png')

plt.figure()
plt.hist(data, histtype='bar')
plt.savefig('histogram.png')

plt.figure()
graph = stats.probplot(data, plot=plt)
plt.savefig('qq-plot.png')

