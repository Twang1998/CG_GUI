from scipy import stats
import pandas as pd
import numpy as np

df1 = pd.read_csv('wangtao.csv')
df2 = pd.read_csv('zzc.csv')
a = np.array((df1['Score']+df2['Score'])/2)
a = np.around(a,2)

df1['Score'] = a
df1.to_csv('Mos.csv',index=False)