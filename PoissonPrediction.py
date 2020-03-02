from scipy.stats import poisson
import seaborn as sb

HomeexpectedTD = input("Enter the expected amount of TDs that the home team will score")
AwayxpectedTD = input("Enter the expected amount of TDs that the away team will score")

data_binom = poisson.rvs(mu=HomeexpectedTD, size=10000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='green',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='TDs', ylabel='Probability')

data_binom = poisson.rvs(mu=AwayexpectedTD, size=10000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='green',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='TDs', ylabel='Probability')