import numpy as np
import pandas as pd
import scipy.stats as st #科学计算包

import statsmodels.api as sm #最小二乘
from statsmodels.formula.api import ols #加载ols模型
import matplotlib.pyplot as plt


t = [1, 3, 5 , 7, 10, 30 , 90, 140]
r = [0.90, 0.70, 0.60, 0.55, 0.40, 0.35, 0.30, 0.25]

data = pd.DataFrame()
data['时间'] = t
data['留存率'] = r
A = 100

#每日新增用户：A   留存率：remain  留存率对应时间

def max_DAU(A, remain, t):
    remain_data = pd.DataFrame(np.array([remain, t]).T, columns = ['remain', 't'])
    #进行对数变换
    remain_data['ln_remain'] = np.log(remain_data['remain'])
    lm = ols('ln_remain ~ t',data=remain_data).fit()
    #print(lm.summary())
    #得到C
    C = np.exp(lm.params['Intercept'])
    #得到a
    a= -lm.params['t']   
    DAU = A*C/a
    print("最大DAU为：{}".format(DAU))   
    return DAU   

