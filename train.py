# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 23:10:35 2017

@author: 羅弘
"""
import pandas as pd
from sklearn.externals import joblib
from sklearn import linear_model
from sklearn.preprocessing import RobustScaler
#from catboost import CatBoostClassifier
# load train data
dic={}

def load_train_fs():
    #default = pd.read_csv(str(sys.argv[1]), index_col = "Train_ID")
    #StartTime	endTime	startX	startY	endX	endY

    default = pd.read_csv("train1.csv", index_col = "Order_ID")
    #print(default['StartTime'])
    default.rename(columns=lambda x:x.lower(),inplace=True)
    default['y'] = default['endtime'].astype('int')
    default.drop('endtime',axis=1,inplace=True)
    default.drop('timestamp',axis=1,inplace=True)
    default.drop('timestampb',axis=1,inplace=True)
    
    default['distance']=(pow((pow((default['startx']-default['endx']),2)+\
           pow(default['starty']-default['endy'],2)),0.5)).astype('float')
    return default
#train arrange
def train_type(train_fs,targetname):
    train_x=train_fs.drop(targetname,axis=1)
    robust_scaler= RobustScaler()
    train_x= robust_scaler.fit_transform(train_x)
    train_y= train_fs[targetname]
    return train_x,train_y
#train model produced
def linearmodel(x_train,y_train):
    global dic
    regr=linear_model.LinearRegression()
    regr.fit(x_train,y_train)
    
#    print(y_train)
    joblib.dump(regr, 'mymodel.joblib')
    model=joblib.load('mymodel.joblib')
    predictions=model.predict(x_train)
    print(predictions)
    return 
# the main function
if __name__ == '__main__':
    train_fs = load_train_fs()

    train_x,train_y = train_type(train_fs,'y')
    linearmodel(train_x,train_y)