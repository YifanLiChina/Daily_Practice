import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from scipy import stats

# N = 6
# k = np.arange(0, N + 1)
p = 0.5

for N in [6, 10, 20]:
    k = np.arange(0, N + 1)
    pdf = stats.binom.pmf(k, N, p)
    plt.plot(k, pdf)

plt.grid(True)
plt.show()
