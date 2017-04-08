# -* - coding:UTF-8 -* -
# 线性回归的预测---离散数据
import StringIO
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

cvs_dt = '''1,2,3
            1,150,6450
            2,200,7450
            3,250,8450
            4,300,9450
            5,350,11450
            6,400,15450
            7,600,18450'''
cvs_dt = unicode(cvs_dt)

data = pd.read_csv(StringIO(cvs_dt))
 #X_parameter = []
 #Y_parameter = []
 # for single_square_feet ,single_price_value in zip(data['square_feet'],data['price']):
 #       X_parameter.append([float(single_square_feet)])
 #       Y_parameter.append(float(single_price_value))
