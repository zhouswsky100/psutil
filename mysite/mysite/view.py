# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render
from psutilModel.models import psutil

def index(request):
    psutilData ={}
    tempData = psutil.objects.values()
    psutilData['list'] = list(tempData)
    print (psutilData['list'])
    return render(request, 'index.html', {'psutilData':psutilData['list']})