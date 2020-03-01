from scipy.stats import poisson
import seaborn as sb

expectedTD = input("Enter the expected amount of TDs that the team will score")

data_binom = poisson.rvs(mu=expectedTD, size=10000)
ax = sb.distplot(data_binom,
                  kde=True,
                  color='green',
                  hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='TDs', ylabel='Probability')