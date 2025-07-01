from sklearn import linear_model
import pandas as pd

reg = linear_model.LinearRegression()
student_data_math = pd.read_csv('./student/student-mat.csv', sep=';')
X = student_data_math.loc[:, ['G1']].values
Y = student_data_math.G3.values

reg.fit(X, Y)

print("回帰係数", reg.coef_)
print("切片", reg.intercept_)
print("数学の回帰モデルのスコア", reg.score(X, Y))
print("-----------------------")
student_data_por = pd.read_csv('./student/student-por.csv', sep=';')
X_por = student_data_por.loc[:, ['G1']].values
Y_por = student_data_por.G3.values

reg.fit(X_por, Y_por)
print("回帰係数 (ポルトガル語)", reg.coef_)
print("切片 (ポルトガル語)", reg.intercept_)
print("ポルトガル語の回帰モデルのスコア", reg.score(X_por, Y_por))