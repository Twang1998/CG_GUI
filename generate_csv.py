import numpy as np
import pandas as pd
import os
import argparse

def arg():
    parser = argparse.ArgumentParser()

    # input parameters
    parser.add_argument('--img_path', type=str)
    parser.add_argument('--csv_file', type=str)

    config = parser.parse_args()

    return config

if __name__ == '__main__':
    config = arg()
    df = pd.DataFrame()

    Image_path = config.img_path
    Pic_List = os.listdir(Image_path)
    # Pic_List = [os.path.join(Image_path,i) for i in Pic_List]

    df['Image'] = Pic_List

    df.to_csv(config.csv_file,index=False)