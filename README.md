### 使用方法

#### 1.生成csv文件
```
python generate_csv.py --img_path 'path_to_img' --csv_file 'xxx.csv'
```
> 注意，这个过程仅需执行一次;当数据集内容做出调整时，例如增删图片，需要重新执行;

#### 2.执行打分
```
python score_GUI.py --mode local --img_path 'path_to_img' --csv_file 'xxx.csv'
```
例如：
```
python score_GUI.py --mode local --img_path C:\Users\37151\Desktop\CGQA\CG_QA --csv_file CG_QA_shuffle.csv
python score_GUI.py --mode internet --img_path http://0.0.0.0/pic/ --csv_file CG_QA_shuffle.csv
python score_GUI.py --mode internet --img_path http://150.158.85.3/CG_QA/CG_QA/ --csv_file CG_QA_shuffle.csv
```
