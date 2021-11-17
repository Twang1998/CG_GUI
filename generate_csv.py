import numpy as np
import pandas as pd
import os

df = pd.DataFrame()

Image_path = 'pic'
Pic_List = os.listdir(Image_path)
# Pic_List = [os.path.join(Image_path,i) for i in Pic_List]

df['Image'] = Pic_List

df.to_csv('Images.csv',index=False)