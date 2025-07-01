import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
student_data_math = pd.read_csv('./student/student-mat.csv', sep=';')
print(student_data_math.head())
#print(student_data_math.info())
print(student_data_math.absences.head())
print(student_data_math.groupby('sex')['age'].mean())

print("平均値", student_data_math.absences.mean())
print("中央値", student_data_math.absences.median())
print("最頻値", student_data_math.absences.mode()[0])

print("分散", student_data_math.absences.var(ddof=0) ) # 母分散
print("標準偏差", student_data_math.absences.std(ddof=0) ) # 母標準偏差
print("標本分散", student_data_math.absences.var(ddof=1) ) # 標本分散
print("標本標準偏差", student_data_math.absences.std(ddof=1))

print("要約統計量", student_data_math.absences.describe())
print("要約統計量", student_data_math.describe())
print("四分位範囲", student_data_math.absences.quantile(0.75) - student_data_math.absences.quantile(0.25))
def show_plt(df):
    plt.hist(df['absences'])
    plt.xlabel('absences')
    plt.ylabel('count')
    plt.grid(True)
    plt.show()

def hakohige0():
    plt.boxplot([student_data_math['G1'], student_data_math.G2, student_data_math.G3])
    plt.grid(True)
    plt.show()

def hakohige1():
    plt.boxplot(student_data_math.absences)
    plt.grid(True)
    plt.show()
#show_plt(student_data_math)
# hakohige0()

print("変動係数", student_data_math.absences.std(ddof=0) / student_data_math.absences.mean())
#print("変動係数", student_data_math.std(ddof=0) / student_data_math.mean())

def scatter_plot(df):
    plt.plot(df.G1_math, df.G3_math, 'o', label='G1 vs G2')
    plt.ylabel('G1')
    plt.xlabel('G2')
    plt.grid(True)
    plt.show()

#scatter_plot()

print("共分散", np.cov(student_data_math.G1, student_data_math.G3, ddof=0))  # 母共分散)
print("G1の分散", student_data_math.G1.var(ddof=0))  # 母分散
print("G3の分散", student_data_math.G3.var(ddof=0))

print(sp.stats.pearsonr(student_data_math.G1, student_data_math.G3))  # ピアソンの積率相関係数
print("相関行列", np.corrcoef([student_data_math.G1, student_data_math.G3]))

student_data_por = pd.read_csv('./student/student-por.csv', sep=';')
print(student_data_por.head())

student_merge_data = pd.merge(student_data_math, student_data_por, 
         on=['school', 'sex', 'age', 'address', 'famsize', 'Pstatus', 
              'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'nursery', 'internet'], 
         how='inner', 
         suffixes=['_math', '_por'])
print(student_merge_data.head())

scatter_plot(student_merge_data)