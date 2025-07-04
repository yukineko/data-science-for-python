import pandas as pd
from scipy import stats

student_mat = pd.read_csv("./student/student-mat.csv", sep=";")
student_por = pd.read_csv("./student/student-por.csv", sep=";")

student_merge = pd.merge(student_mat, student_por, 
                         how="inner", 
                         on=['school', 'sex', 'age', 'address',
                             'famsize', 'Pstatus', 'Medu', 'Fedu',
                             'Mjob', 'Fjob', 'reason', 'nursery',
                             'internet'
                             ],
                             suffixes=('_math', '_por'))
print(student_merge.G1_math.mean())
print(student_merge.G1_por.mean())

t, p = stats.ttest_rel(student_merge.G1_math, student_merge.G1_por)
print("t値:", t)
print("p値:", p)

def null_hypothesis_test():
    # 母平均の差が0であるという帰無仮説を検定
    t, p = stats.ttest_rel(student_merge.absences_math, student_merge.absences_por)
    print("abcences t値:", t)
    print("abcences p値:", p)

    t, p = stats.ttest_rel(student_merge.studytime_math, student_merge.studytime_por)
    print("studytime t値:", t)
    print("studytime p値:", p)


null_hypothesis_test()