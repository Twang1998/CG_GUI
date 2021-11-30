from scipy import stats
import pandas as pd
import numpy as np

df1 = pd.read_csv('wangtao.csv')
df2 = pd.read_csv('zzc.csv')

a = np.array(df1['Score'])
b = np.array(df2['Score'])[:104]

srcc = stats.spearmanr(a,b)[0]
plcc = stats.pearsonr(a,b)[0]
krcc = stats.kendalltau(a,b)[0]

print('srcc: {:.4f}, plcc: {:.4f}, krcc: {:.4f}'.format(srcc,plcc,krcc))