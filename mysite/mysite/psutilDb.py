# -*- coding: utf-8 -*-
from django.http import  HttpResponse

from psutilModel.models import psutil

def psutilDb(request):
    temp = ""
    list = psutil.objects.all()
    for var in list:
        temp = var.cpuCore
    return HttpResponse(temp)
