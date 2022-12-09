# Import packages
from scipy.stats import beta as beta_dist
import matplotlib.pyplot as plt
import numpy as np
# Plot the distribution
alpha = 100_000
beta = 100_000
x = np.arange(0, 1, 0.01)
y = beta_dist.pdf(x, alpha, beta)
plt.figure(figsize=(11, 6))
plt.plot(x, y, linewidth=3)
plt.xlabel('x', fontsize=20)
plt.ylabel('PDF', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.axvline(0.6,  linestyle='dashed', color='black')
plt.savefig('beta_dist.png')
plt.show()
