from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1 = pd.read_csv('wangtao.csv')
df1 = pd.read_csv('zzc.csv')
a = np.array(df1['Score'])

plt.hist(a,bins=50,range=(-0.05,5.05))
plt.xticks(np.arange(0,5,0.1))
plt.show()
