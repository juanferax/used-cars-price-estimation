import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder


def getDict():
    urlUnencoded = "https://drive.google.com/file/d/1Occwzsvdhl2y14B4ehKkoqHjuHURXv7u/view?usp=sharing"
    pathUnencoded = 'https://drive.google.com/uc?export=download&id='+urlUnencoded.split('/')[-2]

    dfUnencoded = pd.read_csv(pathUnencoded)

    df1 = dfUnencoded.pop('price')

    dfUnencoded['price'] = df1

    columns=['bodywork_type','brand','city','color','fuel_type', 'model', 'state','transmission']

    theDict = {}

    for col in columns:
        le = LabelEncoder()
        columnToEncode = dfUnencoded[col]
        columnToEncoded= le.fit_transform(dfUnencoded[col])

        dfUnencoded[col] = columnToEncoded

        iterDict = {}
        for A, B in zip(columnToEncode.values, columnToEncoded):
            iterDict[A] = B

        theDict[col] = iterDict
    
    return theDict


def client_predict(data):
    """
    Parameters
    ----------
    data : list
    List with data (brand  	kilometers 	model 	motor   transmission	year)
    Example: ['Toyota' ,	197000.0 ,	'Land Cruiser' ,	'4.7',  Mecanica 	2002.0]
    
    Returns
    -------
    numpy.float32
    Value predicted
    """

    theDict = getDict()

    xgb_regressor = xgb.Booster({'nthread': 4})  # init model
    xgb_regressor.load_model('trained_final_model.sav')  # load data

    labelsList = ['brand', 'kilometers', 'model', 'motor', 'transmission', 'year']

    dataEncoded = []
    
    count = 0
    
    for colName in labelsList:
        if colName == 'kilometers' or colName == 'year' or colName == 'motor':
            dataEncoded.append(data[count])
        else:
            dataEncoded.append(theDict[colName][data[count]])
        count+=1

    return xgb_regressor.predict(xgb.DMatrix(np.array(dataEncoded).reshape(1,6)))[0]