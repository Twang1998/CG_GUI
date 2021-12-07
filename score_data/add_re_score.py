import pandas as pd
import numpy as np
import json
import os

with open(os.path.join('wangtao.json'),'r') as f:
    Score = json.load(f)

rescore = pd.read_csv('re_score_wt.csv')
indexs = np.array(rescore['index'])
scores = np.array(rescore['Score'])

for i in range(len(indexs)):
    index = indexs[i]
    score = scores[i]
    Score[str(index)] = score

df = pd.read_csv('../CG_QA_shuffle.csv')
Pic_List = np.array(df['Image'])


df = pd.DataFrame(columns=['Index','Image','Score'])

for i in range(6000):
    try:
        # print(i)
        # df.loc[i] = [i,Pic_List[i].split('/')[-1],Score[str(i)]]
        df.loc[i] = [i,Pic_List[i],Score[str(i)]]
    except:
        pass
df.to_csv(os.path.join('wangtao1.csv'),index=False)