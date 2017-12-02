import os
# import csv
import requests
import pandas as pd

path = './pandas/data/'
'''
下载数据集并保存到本地
'''
source = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
with open(path+'iris.txt','w') as f:
    f.write(source.text)
# 读取数据集
df = pd.read_csv(path+'iris.txt',names=['sepql_length','sepal_width','petal_length','petal_width','class'])
'''查看dataframe某一列的数据'''
# data = df['class'].head()
'''使用.ix[row,column]查看dataframe的部分数据'''
# data = df.ix[:4,2:]
# data = df.ix[:4,[c for c in df.columns if 'width' in c]]
'''查看dataframe某列去重后的数据'''
# data = df['class'].unique()
'''对dataframe求和,str也可以求和'''
# data = df.sum()
'''查看dataframe某一类的数据'''
# data = df[df['class']=='Iris-setosa'].head()
# data = df[(df['class']=='Iris-setosa')&(df['petal_width']<0.2)].head()
'''查看dataframe的描述性统计'''
# data = df.describe()
'''查看dataframe各个特征之间的相关性,默认是pearson相关系数,可以通过method参数指定Kendall或spearman系数'''
# data = df.corr()
# data = df.corr(method='kendall')
# data = df.corr(method='spearman')

print(data)
