# -*- coding: utf-8 -*-
from django.db import models

class psutil(models.Model):
    ip = models.CharField(max_length=20)
    sysDate = models.CharField(max_length=20)
    sysOpenDate = models.CharField(max_length=20)
    cpuLineCity = models.CharField(max_length=20)
    cpuCore = models.CharField(max_length=20)
    cpuPer = models.CharField(max_length=20)
    allRam = models.CharField(max_length=5)
    remainRam = models.CharField(max_length=20)
    perRam = models.CharField(max_length=20)
    allStorage = models.CharField(max_length=20)
    remainStorage = models.CharField(max_length=20)
    perStorage = models.CharField(max_length=20)
    state = models.CharField(max_length=20)


