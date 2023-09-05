import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#sample size
n = 375
#hypothetical population mean
m = 0.53
#observed mean
o = 0.79
#generate the simulated null distribution
null_outcomes = []
for i in range(100000):
    simulation = np.random.choice(['buy','leave'], size=n, p=[m, 1-m])
    num_purcahsed = np.sum(simulation == 'buy')
    null_outcomes.append(num_purcahsed)
null_outcomes = np.array(null_outcomes)

observed = n*o
expected = n*m
p_value = np.sum(null_outcomes >= observed)/len(null_outcomes)


#Plot the null distribution as a histogram
# Include vertical lines at the purchase rates 
sns.histplot(null_outcomes, bins=75)
plt.suptitle('Null Distribution')
plt.title(f'100,000 Samples, n={n}, μ={m}')
plt.xlabel("Users Who Made a Purchase")
plt.axvline(expected, color='black', linestyle = '--', label='Control')
plt.text(expected+0.3,7100,f'{100*m}%',rotation=90)
plt.axvline(observed, color='cyan', linestyle = '--', label='Variant')
plt.legend()
plt.text(observed+0.3,7100,f'{100*o}%',rotation=90)
plt.savefig("null_dist.png")

print(f'p-value = {p_value}')
