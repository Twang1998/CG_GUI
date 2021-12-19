from scipy import stats
import pandas as pd
import numpy as np

df1 = pd.read_csv('wangtao.csv')
df2 = pd.read_csv('zzc.csv')
df3 = pd.read_csv('wangtao2.csv')
df4 = pd.read_csv('zzc2.csv')
a = np.array((df1['Score']+df2['Score']+df3['Score']+df4['Score'])/4)
a = np.around(a,2)

df = pd.DataFrame()
df['Index'] = df1['Index']
df['Image'] = df1['Image']

df['wangtao'] = df1['Score']
df['zzc'] = df2['Score']
df['wangtao2'] = df3['Score']
df['zzc2'] = df4['Score']
df['MOS'] = a

df.to_csv('MOS_all.csv',index=False)