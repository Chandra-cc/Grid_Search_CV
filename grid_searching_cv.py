# -*- coding: utf-8 -*-
"""Grid_searching_cv

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-jBSXo0AjOPA1_lVx3gs4OK8CYjwPmvE
"""

! pip install kaggle

! mkdir ~/.kaggle

! cp kaggle.json ~/.kaggle/

! chmod 600 ~/.kaggle/kaggle.json

! kaggle datasets download rashikrahmanpritom/heart-attack-analysis-prediction-dataset

! unzip /content/heart-attack-analysis-prediction-dataset.zip

import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

data=pd.read_csv("/content/heart.csv")

data

X,y=data.iloc[:,:-1],data.iloc[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,stratify=y,random_state=48)

X_train.shape

X_test.shape

model=SVC()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy_score(y_test,y_pred)

param_grid={
    'C':[0.1,1,10,100,1000],
    'kernel':['rbf'],
    'gamma':[10,1,0.1,0.01,0.001,0.0001],
}

grid=GridSearchCV(SVC(),param_grid,scoring='accuracy',refit=-True,verbose=3)
grid.fit(X_train,y_train)

pred=grid.predict(X_test)
accuracy_score(y_test,pred)

grid.best_estimator_

