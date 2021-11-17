### 使用方法

#### 1.生成csv文件
```
python generate_csv.py --img_path 'path_to_img' --csv_file 'xxx.csv'
```
> 注意，这个过程仅需执行一次;当数据集内容做出调整时，例如增删图片，需要重新执行;

#### 2.执行打分
```
python score_GUI.py --img_path 'path_to_img' --csv_file 'xxx.csv'
```
