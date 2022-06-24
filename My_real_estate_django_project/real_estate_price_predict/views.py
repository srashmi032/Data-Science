from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from polls.models import Price

from joblib import dump, load
import numpy as np

model=load('/Users/rashmi/Desktop/djproj/project1/polls/My_house_predictor.joblib')


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")# Create your views here.
    return render(request, 'index.html')


def predict(request):
    if request.method == 'POST':
        CRIM=request.POST.get('1')
        ZN=request.POST.get('2')
        INDUS=request.POST.get('3')
        CHAS=request.POST.get('4')
        NOX=request.POST.get('5')
        RM=request.POST.get('6')
        AGE=request.POST.get('age')
        DIS=request.POST.get('8')
        RAD=request.POST.get('9')
        TAX=request.POST.get('10')
        PTRATIO=request.POST.get('11')
        B=request.POST.get('12')
        LSTAT=request.POST.get('13')
        print(CRIM)
        price=Price(CRIM=CRIM)
        price.save()

        features=np.array([[CRIM,ZN,INDUS,CHAS,NOX,RM, AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
        price_pred=model.predict(features)

        messages.success(request, 'Your message has been sent!')
        house_price={'hprice':price_pred}


    return render(request, 'price.html',house_price)
