# coding: utf-8
import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
#加上一个微小值delta，当出现y为0的情况时，避免负无穷大的发生
t=np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
y=np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])

print(cross_entropy_error(y,t))#0.51082545709933802

y=np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])
print(cross_entropy_error(y,t))#2.302584092994546