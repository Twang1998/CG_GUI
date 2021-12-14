from scipy import stats
import pandas as pd
import numpy as np

df1 = pd.read_csv('wangtao.csv')
df2 = pd.read_csv('wangtao2.csv')

a = np.array(df1['Score'])[0:3000]
b = np.array(df2['Score'])[0:3000]
# a = (a+b)/2

srcc = stats.spearmanr(a,b)[0]
plcc = stats.pearsonr(a,b)[0]
krcc = stats.kendalltau(a,b)[0]
rmse = np.sqrt(np.mean((a-b)**2))

print('srcc: {:.4f}, plcc: {:.4f}, krcc: {:.4f}, rmse: {:.4f}'.format(srcc,plcc,krcc,rmse))