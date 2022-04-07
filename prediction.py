import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle
symptoms = pd.read_csv("training.csv")
symptoms.head()
lables=symptoms.columns.to_list()
def split_train_test(data,test_ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    print(shuffled)
    test_set_size = int(len(data)*test_ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]
    
#LabelEncoder
le = LabelEncoder()
for i in symptoms.prognosis:
    print(i)
symptoms.prognosis = le.fit_transform(symptoms.prognosis)
for i in symptoms.prognosis:
    print(i)

#symptoms
#symptoms.describe()

train_set,test_set = split_train_test(symptoms,0.2)

#(len(train_set))
#(len(test_set))

train_set_tr=train_set.copy()
train_lables=train_set['prognosis']
del train_set_tr['prognosis']
#train_set_tr

test_set_tr=test_set.copy()
test_lables=test_set['prognosis']
del test_set_tr['prognosis']
#print(lables)

model = LinearRegression()
model.fit(train_set_tr,train_lables)

file = open('model.pkl','wb')
pickle.dump(model,file)
file.close()

#symp_prediction = model.predict(train_set_tr)
#lin_mse = mean_squared_error(train_lables,symp_prediction)
#lin_rmse = np.sqrt(lin_mse)

#lin_rmse

test_data = test_set_tr.iloc[:]
test_lable = test_lables.iloc[:]
print(test_lable)

#print(model.predict(test_data))
#print(test_lable)
#test_lable


