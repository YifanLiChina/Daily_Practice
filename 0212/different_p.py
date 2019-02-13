import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from scipy import stats

# p = 0.5
N = 6
k = np.arange(0, N + 1)

for p in [0.1, 0.3, 0.5, 0.7, 0.9]:
    pdf = stats.binom.pmf(k, N, p)
    plt.plot(k, pdf)

plt.grid(True)
plt.show()
