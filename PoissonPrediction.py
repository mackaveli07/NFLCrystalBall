from scipy.stats import poisson
import seaborn as sb


HomeExpectedTD = input("Enter the expected amount of TDs that the home team will score")
AwayExpectedTD = input("Enter the expected amount of TDs that the away team will score")

data_binom = poisson.rvs(mu=HomeExpectedTD, size=10000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='green',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='TDs', ylabel='Probability')



data_binom2 = poisson.rvs(mu=AwayExpectedTD, size=10000)

ax = sb.distplot(data_binom,
                  kde=True,
                  color='green',
                  hist_kws={"linewidth": 25,'alpha':1})

ax.set(xlabel='TDs', ylabel='Probability')


