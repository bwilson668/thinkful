import pandas as pd

# data setup
data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.12,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Norther Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# data analysis
print "Alcohol mean:", df['Alcohol'].mean()
print "Alcohol median:", df['Alcohol'].median()
print "Alcohol mode:", df['Alcohol'].mode()
print "Alcohol range:", max(df['Alcohol']) - min(df['Alcohol'])
print "Alcohol standard deviation:", df['Alcohol'].std()
print "Alcohol variance:", df['Alcohol'].var()

print "\n"

print "Tobacco mean:", df['Tobacco'].mean()
print "Tobacco median:", df['Tobacco'].median()
print "Tobacco mode:", df['Tobacco'].mode()
print "Tobacco range:", max(df['Tobacco']) - min(df['Tobacco'])
print "Tobacco standard deviation:", df['Tobacco'].std()
print "Tobacco variance:", df['Tobacco'].var()
