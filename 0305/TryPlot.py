import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

year=[1950,1970,1990,2010]
pop=[2.518,3.68,5.23,6.97]
# 1.线图
#调用plt。plot来画图,横轴纵轴两个参数即可
plt.plot(year,pop)
# python要用show展现出来图
plt.show()
