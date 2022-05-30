# -*- coding: utf-8 -*-
"""loss_functins.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oLJZd9GCvQ96gd9OxsLr-5LR3wsDrWII
"""

import numpy as np
y_pred = np.array([1,1,0,0,1])
y_t = np.array([0.3,0.7,1,0,0.8])

def mae(y_t,y_pred):
  tot_err = 0
  for yt,yp in zip(y_t,y_pred):
    print(yt,yp)
    tot_err+= abs(yt-yp)

  print('Total MA Error : ', tot_err)
  mae = tot_err/len(y_t)
  return mae

mae(y_t,y_pred)

np.mean(np.abs(y_t - y_pred))

np.sum(np.abs(y_t - y_pred))

np.log([0.000000000000000001])

epsilon = 1e-15
epsilon

print(y_pred, end = ',\n')
yp_new = [max(i,epsilon) for i in y_pred]
yp_new

yp_new = [max(i,epsilon) for i in y_pred]
yp_new

yp_new = [min(i,1-epsilon) for i in yp_new]
yp_new

yp_new = np.array([yp_new])
np.log(yp_new)

loss = -np.mean(y_t*np.log(yp_new) + (1-y_t)*np.log(1-yp_new))
loss

def log_loss(y_t,y_pred):
    epsilon = 1e-15
    yp_new = [max(i,epsilon) for i in y_pred]
    yp_new = [min(i,1-epsilon) for i in yp_new]
    yp_new = np.array([yp_new])
    return -np.mean(y_t*np.log(yp_new) + (1-y_t)*np.log(1-yp_new))

log_loss(y_t,y_pred)
