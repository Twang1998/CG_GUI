from scipy import stats
import pandas as pd
import numpy as np

df_all = pd.read_csv('MOS_all.csv')

test_list = pd.read_csv('../CG_QA_test.csv')
test_img_list = np.array(test_list['Image']).tolist()

# res = df_all[df_all['Image'] in test_img_list]

# print(res)
res = pd.DataFrame(columns=['Index','Image','wangtao','zzc','wangtao2','zzc2','MOS'])
for i,img in enumerate(test_img_list):
    index = np.where(np.array(df_all['Image']) == img)[0][0]
    # print(index)

    res.loc[i] = df_all.iloc[index]

res.to_csv('MOS_test.csv',index=False)
