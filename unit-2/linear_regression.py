import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(str(x)[:3]))
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(str(x)[:-1]))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(str(x)[:-7]))

plt.figure()
p = loansData['Interest.Rate'].hist()
plt.show()

a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
