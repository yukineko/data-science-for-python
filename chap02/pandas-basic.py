import pandas as pd
import numpy as np
from pandas import Series, DataFrame

sample_pandas_data = pd.Series(np.array([0,10,20,30,40,50,60,70,80,90]))
print(sample_pandas_data)

sample_pandas_data2 = pd.Series(
    np.array([0,10,20,30,40,50,60,70,80,90]),
    index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    )
print(sample_pandas_data2)
print(sample_pandas_data2.index)

attr1_data = {
    'ID': [100,200,300,400,500],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
attr1_data_frame = DataFrame(attr1_data)
print(attr1_data_frame)

attr1_index = DataFrame(attr1_data, index=['a', 'b', 'c', 'd', 'e'])
print(attr1_index)
print(attr1_index.T) #転置
print('------------------------')
print(attr1_index.Name) 
print(attr1_index['City'] == 'New York') #条件でフィルタリング
print(attr1_index[attr1_index['City'] == 'New York']) #条件でフィ
print(attr1_index[attr1_index['City'].isin(['New York', 'Chicago'])]) #条件でフィ
print('------------------------')

print(attr1_index.sort_values(['City', 'Name']))
print(attr1_index.City.sort_values()) #昇順と降順の指定

print(attr1_data_frame.Age.sum(),
      attr1_data_frame.Age.mean()) #平均値

attr2_data = {
    'ID': [1,2,3,4,5], 
    'Name': ["Saito", 'Horie', 'Kondo','Kawada', 'Matsushita'],
    'Money':[1000,2000,500,300,700], 
    'Gender': ['M', 'M', 'F', 'M', 'F'],
}

attr2_data_frame = DataFrame(attr2_data)
#print(attr2_data_frame.Gender.isin('M').mean())
print(attr2_data_frame.groupby('Gender')['Money'].mean()) #性別ごとの平均値
print(attr2_data_frame.Money.gt(500))
print(attr2_data_frame.iloc[[2,3]])
print(attr2_data_frame[attr2_data_frame.Money > 500] )

attr3_data = {
    'ID': [3,4,7],
    'Math': [80, 90, 70],
    'English': [70, 80, 90],
}
attr3_data_frame = DataFrame(attr3_data)
composed = pd.merge(attr2_data_frame, attr3_data_frame, on='ID', how='outer')
print(composed)