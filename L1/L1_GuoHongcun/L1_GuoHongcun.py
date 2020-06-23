'''Action1: 求2+4+6+8+...+100的求和
'''
import numpy as np
import pandas as pd

a = np.arange(2, 102, 2)
sumA = sum(a)
print('action1:\n 2+4+6+8+...+100=%d\n' % sumA)

'''Action2: 统计全班的成绩
班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、最小成绩、
最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出（可以用numpy或pandas）
'''

data1 = {'Chinese': [66, 95, 93, 90, 80], 'Math': [30, 98, 96, 77, 90], 'English': [65, 85, 92, 88, 90]}
df1 = pd.DataFrame(data1, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'],
                   columns=['Chinese', 'Math', 'English'])
print('*****************\naction2:\n原始数据：')
print(df1)
print('成绩描述：')
VAR = df1.var()
df3 = df1.describe(include=['number']).loc[['min', 'max', 'mean', 'std']].T
df2 = pd.DataFrame(VAR, columns=['var'])
df3 = pd.concat([df3, df2], axis=1)
print(df3)
print('总成绩排序:')
df1['Col_sum'] = df1.apply(lambda x: x.sum(), axis=1)
print(df1.sort_values('Col_sum', ascending=False))

'''Action3: 
对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多
'''
# df4 = pd.read_csv('car_complain.csv')
# # print(df4)
# df4 = df4.drop()
result = pd.read_csv('car_complain.csv')
# print(result.drop('problem', 1))
# print(result.problem.str.get_dummies(','))
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))  # pandas.Series.str.get_dummies拆分series中以","分隔的字符串，然后返回一个DataFrame对象。

# 品牌投诉总数并排列:
result1 = result.groupby(['brand'])['id'].agg(['count'])
print('\n*****************\naction3:\n品牌投诉总数并排列:')
print(result1.sort_values('count', ascending=False))

# 车型投诉总数并排列:
result2 = result.groupby(['car_model'])['id'].agg(['count'])
print('车型投诉总数并排列:')
print(result2.sort_values('count', ascending=False))

# 品牌的平均车型投诉排列：
result3 = result.groupby(['brand', 'car_model'])['id'].agg(['count'])
result3 = result3.groupby('brand').mean()
print('品牌的平均车型投诉排列:')
print(result3.sort_values('count', ascending=False))

