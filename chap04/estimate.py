import numpy as np
from scipy.stats import t

def t_value(data, alpha=0.05):
    # 自由度
    df = len(data) - 1

    # 両側で5%だから片側2.5%
    tail = alpha / 2

    # 上側2.5%点は 97.5%分位点
    t_value = t.ppf(1 - tail, df)
    return t_value

data = [170, 172, 168, 169, 171, 173, 167, 170, 172, 169]
print("t値:", t_value(data) )

def confidence_interval(data, alpha=0.05):
    size = len(data)
    mean = np.mean(data)
    std = np.std(data, ddof=1)
    t_val = t_value(data, alpha)
    se = std / np.sqrt(size)

    lower = mean - t_val * se
    upper = mean + t_val * se
    return lower, upper

print(confidence_interval(data))


