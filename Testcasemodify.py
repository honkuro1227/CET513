import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import RobustScaler

dic={}

def distance(s,d):
    x1=s[0]
    y1=s[1]
    x2=d[0]
    y2=d[1]
    return pow((pow(abs(x1-x2),2)+pow(abs(y1-y2),2)),1/2)
def rideshare(a,p):
    global R, hotspot
    startds=pow((pow(a['startx'][p]-hotspot['a'][0],2)+pow(a['starty'][p]-hotspot['a'][1],2)),0.5)
    endds=pow((pow(a['endx'][p]-hotspot['b'][0],2)+pow(a['endy'][p]-hotspot['b'][1],2)),0.5)
    if startds<=R and endds<=R:
        return (startds,endds)
    else:
        return False

def load_test_fs():
    default = pd.read_csv("test1102.csv", index_col = "Order_ID")
    default.rename(columns=lambda x:x.lower(),inplace=True)
    default['y'] = default['endtime'].astype('int')
    default.drop('endtime',axis=1,inplace=True)
    default.drop('timestamp',axis=1,inplace=True)
    default.drop('timestampb',axis=1,inplace=True)
    distance=(pow((pow(default['startx']-default['endx'],2)+pow(default['starty']-default['endy'],2)),0.5))
    default['distance']=distance.astype('float')
    return default
    
def test_type(test_fs):
    x_Test=test_fs
    robust_scaler= RobustScaler()
    x_Test= robust_scaler.fit_transform(x_Test)
    
    return x_Test

def output_mfs(fs,name):
    result=fs.iloc[:]
    result.to_csv(name+'.csv', encoding='utf-8', index=False)
    return

def test_id(test_fs,filename):
    default= pd.read_csv(filename)
    x_Test = default['Order_ID']
    return x_Test

def linearmodel(x_test,x_id):
    model=joblib.load('mymodel.joblib')
    y_pred_prob=model.predict(x_test)
    dic={
            "Order_ID":x_id,
            "Cost":y_pred_prob
            }
    return  pd.DataFrame(dic)
# the main function
if __name__ == '__main__':
    test_fs=load_test_fs()
    ptestid= test_id(test_fs,"test1102.csv")
    test_fs=test_fs.drop('y',axis=1)
    x_test  = test_type(test_fs)
    output_mfs(linearmodel(x_test,ptestid),'test1102output')


