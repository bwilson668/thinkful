import numpy as np
import pandas as pd
import statsmodels.api as sm

loansData = pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')

loansData['FICO.Score'] = loansData['FICO.Range'].map(lambda x: int(str(x)[:3]))
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: float(str(x)[:-1]))
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda x: int(str(x)[:-7]))

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

loansData.to_csv('loansData_clean.csv', header=True, index=False)

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1, x2])

X = sm.add_constant(x)
model = sm.OLS(y, x)
f = model.fit()
print f.summary()
