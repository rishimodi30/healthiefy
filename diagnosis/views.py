

# Create your views here.
from asyncio.windows_events import NULL
from pyexpat import model
from wsgiref.util import request_uri
from xml.etree.ElementTree import tostring
from django.shortcuts import redirect, render
from django.http import HttpResponse
import pickle
import prediction
import numpy as np;


file = open('model.pkl','rb')
model=pickle.load(file)
file.close
#true=np.array_str(prediction.test_lable)
main=prediction.lables
prediction.lables.sort()

def diagnosis(request):
    
    if request.method=='POST':
      
      base = request.POST.getlist('chk_dis[]')
      raw_list=[]
      for i in main:
          
          if i in base:
              raw_list.append(1)
          else:
              raw_list.append(0)       
          
      raw_list.pop()
      fin_np = np.array(raw_list)

      fin_np=fin_np.reshape(1,-1)
      data=predict_res(fin_np)
      return render(request,'diagnosis.html',{'lables':prediction.lables,'data':data})
  
    
    return render(request,'diagnosis.html',{'lables':prediction.lables})


def predict_res(fin_np):

    # symp_prediction = model.predict(train_set_tr)
    #lin_mse = mean_squared_error(train_lables,symp_prediction)
    #lin_rmse = np.sqrt(lin_mse)
    #lin_rmse
    #test_data = [1,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,
     #            1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,
      #           1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,1,1]
    
    #test_lable = test_lables.iloc[30:40
    #print("called")

    data=np.array_str(model.predict(fin_np))
    
    return data