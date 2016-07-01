import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('loansData_clean.csv')

df['IR_TF'] = df['Interest.Rate'].map(lambda x: 1 if x >= 12 else 0)
df['Intercept'] = df['Interest.Rate'].map(lambda x: 1)

ind_vars = df.columns.values

print ind_vars

logit = sm.Logit(df['IR_TF'], df[ind_vars])
result = logit.fit()
coeff = result.params
print coeff
