# -*- coding: utf-8 -*-
"""Data_Viz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZDhpO6BfQdGus35uCG2Za6CTsT8DSwlR
"""

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.array([x for x in range(1,32)])
x
y1 = np.random.randint(30,45,31)
y2 = np.random.randint(40,46,31)

plt.plot(x,y1, 'r*--', label='Y1 TempLine')
plt.plot(x,y2, 'b+--', label=' Y2 TempLine')
plt.title('Temperature Graph', fontsize=15)
plt.xlabel('Days')
plt.legend(loc = 4)
plt.grid('b--')
plt.ylabel('Temperature')
plt.show()

#Histogram
ml = np.random.randint(21,30,100)
py = np.random.randint(18,45,200)

bins = [15,20,25,30,35,40,45,50]
plt.hist(ml, bins, color = 'b', rwidth = 0.9, label = 'ML Students')
plt.hist(py, bins, color = 'y', rwidth = 0.9, label = 'Py Students')

plt.xlabel('Students Age')
plt.ylabel('No. of Students')
plt.legend()

bins = [15,20,25,30,35,40,45,50]
plt.hist([ml,py], bins, color = ['b','y'] , rwidth = 0.9, label= ['ML Students', 'Py Students'])
#plt.hist(py, bins, color = 'y', rwidth = 0.9)
plt.legend()
plt.xlabel('Students Age')
plt.ylabel('No. of Students')

#Bar chart
sub = ['Python', 'C', 'C++', 'Java','DS', 'JS']
c1 = np.random.randint(10,40,6)
c2 = np.random.randint(15,35,6)
c3 = np.random.randint(20,30,6)
c4 = np.random.randint(10,30,6)

width = 0.2
sub_index = np.arange(len(sub))
plt.bar(sub_index,c1,width,color='y',alpha=0.7,label='C1 Students')
plt.bar(sub_index+width,c2,width,color='b',alpha=0.7,label='C2 Students')
plt.bar(sub_index+width+width,c3,width,color='r',alpha=0.7,label='C3 Students')
plt.bar(sub_index+width+width+width,c4,width,color='g',alpha=0.7,label='C4 Students')
plt.xticks(sub_index+width+width, sub)
plt.legend()

#scatter plot
df = pd.read_csv('/content/googleplaystore.csv', nrows = 2000)
df = df.iloc[:,1:]
df.head()
r,c = df.shape

x = df['Rating']
y = df['Reviews']

#plt.figure(figsize=(9,9))
plt.scatter(x,y, c= 'y', marker = '*')
plt.scatter(x,df['Installs'], c= 'b', marker = 'o')
plt.xlabel('Rating')
plt.ylabel('Reviews')



from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for i in range(0,c):
    df.iloc[:,i] = encoder.fit_transform(df.iloc[:,i])  
    
df.head()

X = df.drop('Installs', axis = 1)
Y = df['Installs']
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score as accuracy, mean_squared_error as mse, confusion_matrix as cm
x_tr,x_t,y_tr,y_t = train_test_split(X,Y, test_size = 0.2, random_state =123)

def svm(x_tr,y_tr,x_t,y_t):
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC
    svmclf = make_pipeline(StandardScaler(), SVC (gamma = 'auto'))
    svmclf.fit(x_tr,y_tr)
    y_pred = svmclf.predict(x_t)
    y_pred
    svm_accuracy = accuracy(y_t,y_pred)
    accuracy
    print(f'Accuracy of SVM : {svm_accuracy}')
    cm(y_t,y_pred)
    print('CM : ',cm)

svm(x_tr,y_tr,x_t,y_t)

def decision_tree(x_tr,y_tr,x_t,y_t):
    from sklearn import tree
    from sklearn.tree import DecisionTreeClassifier
    decisionclf = DecisionTreeClassifier()
    decisionclf.fit(x_tr,y_tr)
    y_pred = decisionclf.predict(x_t)
    tree_accuracy = accuracy(y_t,y_pred)
    print(f'Accuracy of Decision Tree : {tree_accuracy}')
    cm(y_t,y_pred)
    print('CM : ',cm)

decision_tree(x_tr,y_tr,x_t,y_t)

from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(x_tr,y_tr)
y_pred = clf.predict(x_t)
lin_mse = mse(y_t,y_pred)
print('Linear Regression MSE : ', lin_mse)



