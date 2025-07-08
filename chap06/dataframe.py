import pandas as pd
import numpy as np

def sample():
    hier_df = pd.DataFrame(
        np.arange(9).reshape(3, 3),
        index=[['a', 'a', 'b'], [1,2,2]],
        columns=[['Osaka', 'Tokyo', 'Osaka'],['Blue', 'Red', 'Red'] 
        ])

    hier_df.index.names = ['key1', 'key2']
    hier_df.columns.names = ['city', 'color']
    print(hier_df)

    print(hier_df['Osaka'])

def practice601():
    hier_df = pd.DataFrame(
        np.arange(12).reshape((3, 4)),
        index=[['c', 'd', 'd'], [1, 2, 1]],
        columns=[
            ['Kyoto', 'Nagoya', 'Hokkaido', 'Kyoto'],
            ['Yellow', 'Yello', 'Red', 'Blue']]
    )
    hier_df.index.names = ['key1', 'key2']
    hier_df.columns.names = ['city', 'color']
    print(hier_df.groupby(by=['city']).mean())

#practice601()

def combine():
    data1 = {
        'id': ['100', '101', '102', '103', '104', '106', '108', '110', '111', '113'],
        'city': ['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo', 'Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
        'birth_year': [1990, 1985, 1992, 1988, 1990, 1991, 1987, 1993, 1989, 1990],
        'name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    }
    df1 = pd.DataFrame(data1)

    data2 = {
        'id': ['100', '101', '102', '105', '107'],
        'math': [50,43,33,76,90],
        'english': [60,70,80,90,100],
        'gender': ['M', 'F', 'M', 'F', 'M'],
        'index_number': [0, 1, 2, 3, 4]
    }
    df2 = pd.DataFrame(data2)

    df3 = pd.merge(df1, df2, on='id', how='outer') 
#    print(df3)
    df4 = pd.merge(df1, df2, left_index=True, right_on='index_number')
    print(df4)
combine()