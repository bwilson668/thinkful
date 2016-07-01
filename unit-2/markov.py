import pandas as pd

df = pd.DataFrame({'rainy': [.4, .7],
                   'sunny': [.6, .3]
                   },
                  index=["rainy", "sunny"])

print df
print df.dot(df)
print df.dot(df).dot(df)

market = pd.DataFrame({'bull': [.9, .075, .025],
                       'bear': [.15, .8, .05],
                       'stagnant': [.25, .25, .5]
                       },
                      index=["bull", "bear", "stagnant"])

for i in range(1, 11):
    market = market.dot(market)
    print "\ntransition " + str(i)
    print market
