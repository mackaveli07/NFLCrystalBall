from scipy.stats import poisson
import matplotlib.pyplot as plt

plt.ylabel('Probabilty')
plt.xlabel('Number of TD')
plt.title('Probability of # of TDs')
arr = []
arr2= []
HomeExpectedTD = int(input("What is the expected TD for the home team:"))
AwayExpectedTD = int(input("What is the expected TD for the away team:"))
rv = poisson(HomeExpectedTD)
rv2 = poisson(AwayExpectedTD)
for num in range(0, 5):
    arr.append(rv.pmf(num))
    arr2.append(rv2.pmf(num))

# print(rv.pmf(28))
prob = rv.pmf(5)
plt.grid(True)
plt.plot(arr, linewidth=2.0)
plt.plot(arr2, linewidth=2.0)
plt.plot([5], [prob], marker='o', markersize=6, color="red")
plt.show()
