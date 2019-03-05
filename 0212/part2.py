import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from scipy.special import comb

# the type of coin which is specified with
# the probability of landing on heads
p = [0 for i in range(0,101)]
for i in range(0,101):
    p[i] = i/100

# compute the likelihood for each type of coin
f = [0 for i in range(0,101)]
for i in range(0,101):
    f[i] = comb(6,2)*(p[i]**2)*((1-p[i])**4)

# ML = max(f)
# MLE = p[f.index(ML)]
# print(ML)
# print(MLE)
#
# plt.plot(p, f)
# plt.xlabel('types of coin: the probability of landing on heads')
# plt.ylabel('likelihood of the observed sequence')
# plt.grid(True)
# plt.show()

# compute the Posteriori for each type of coin
fp = [0 for i in range(0,101)]
for i in range(0,101):
    fp[i] = f[i] * (1/101)
# s = sum(fp)
# # for i in range(0,101):
# #     fp[i] = fp[i]/s

MAP = max(fp)
MAPE = p[fp.index(MAP)]
print(MAP)
print(MAPE)


plt.plot(p, fp)
plt.xlabel('types of coin: the probability of landing on heads')
plt.ylabel('likelihood of the observed sequence')
plt.grid(True)
plt.show()

