# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
from joblib import load
from sklearn import linear_model
from sklearn.preprocessing import RobustScaler
# load test data
def load_test_fs(filename):
    default = pd.read_csv("Train1.csv", index_col = "Order_ID")
    default.rename(columns=lambda x:x.lower(),inplace=True)
    default['cost'] = (default['endtime']-default['starttime']).astype('int')
    default['distance']=(pow((pow(default['startx']-default['endx'],2)+pow(default['starty']-default['endy'],2)),0.5)).astype('float')
    return default

def output_preds(preds,name):
    result=preds.iloc[:,0:1]
    result.to_csv(name+'.csv', encoding='utf-8', index=False)
    return

# extract features from test data
def test_type(test_fs):
    x_Test=test_fs
    robust_scaler= RobustScaler()
    x_Test= robust_scaler.fit_transform(x_Test)
    return x_Test

def test_id(test_fs,filename):
    #default= pd.read_csv(str(sys.argv[2]))
    default= pd.read_csv(filename)
    x_Test = default['Order_ID']
    return x_Test


def linearmodel(x_test,x_id):
    model=load("mymodel.joblib")
    y_pred_prob=model.predict(x_test)
    dic={
            "Order_ID":x_id,
            "cost":y_pred_prob
            }
    return  pd.DataFrame(dic).sort_values(by=['cost'],ascending=False)


# the main function
if __name__ == '__main__':
    ptest_fs= load_test_fs("test1102.csv")
    ptest_x = test_type(ptest_fs)
    ptestid= test_id(ptest_fs,"test1102.csv")
    output_preds(linearmodel(ptest_x,ptestid),'public')


