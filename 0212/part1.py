import numpy as np
# came across an error when trying to import matplotlib.pyplot:
# "libc++abi.dylib:terminating with uncaught exception of type NSException"
# fixed with https://stackoverflow.com/questions/46660548/i-have-an-error-
# when-importing-modules-using-pycharm-that-does-not-occur-when-us?rq=1
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from scipy import stats

# Define N, p, k
# "For a sequence of N such events, the Binomial distribution
# gives the probability of observing k times the outcome that
# occurs with the probability p"
N = 6
p = 0.5
k = np.arange(0, N + 1)  # seven possible outcomes

pdf = stats.binom.pmf(k, N, p)  # probability density/mass function.
cdf = stats.binom.cdf(k, N, p)  # cumulative density function

ppdf, = plt.plot(k, pdf, label='pdf (N=6, p=0.5)')
pcdf, = plt.plot(k, cdf, label='cdf (N=6, p=0.5)')

# got an error when trying to plot legends of two lines in one figure:
# " 'list' object has no attribute 'get_label'"
# fixed with https://stackoverflow.com/questions/
# 36329269/python-legend-attribute-error
plt.legend(handles=[ppdf, pcdf], loc='best')
plt.grid(True)
plt.show()
