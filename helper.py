import pickle
import numpy as np

model=pickle.load(open('model.pkl', 'rb'))
df_pivit=pickle.load(open('pivit-table.pkl', 'rb'))





def title():
    a=df_pivit.index.values.tolist()
    a.insert(0,'Select Title')
    return a


def books(text):
    a=np.where(df_pivit.index==str(text))[0][0]
    distancees,suggeion=model.kneighbors(df_pivit.iloc[a,:].values.reshape(1,-1),n_neighbors=6)
    for i in range(len(suggeion)):
        b=df_pivit.index[suggeion[i][1:]]
        # print(b)
        first,sec,third,forth,fifth=b[0],b[1],b[2],b[3],b[4]
    return first,sec,third,forth,fifth
