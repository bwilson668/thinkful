import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import collections

model = pd.read_csv('./chi_squared_data.csv')

print model['expected']

observed_freq = collections.Counter(model['observed'])
expected_freq = collections.Counter(model['expected'])

# need to build up both of these arrays to match in size... loop over range 0 to 60

plt.figure()
plt.bar(observed_freq.keys(), observed_freq.values(), width=1)
plt.show()

chi, p = stats.chisquare(observed_freq, f_exp=expected_freq)
print chi
print p
