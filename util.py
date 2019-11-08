#coding:utf-8
from __future__ import division
import psutil
import os
import sys
import pymysql
import datetime
import time
import socket
import schedule
import string


def inspectionJob():
    # 先获取计算机名
    name = socket.gethostname()
    # 计算机名获取ip
    ip = socket.gethostbyname(name)
    #print(u"in当前计算机IP %s " % ip)

    # 当前系统时间
    sysDate = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
    #print(u"in当前系统时间 %s " % sysDate)

    # 系统启动时间
    sysOpenDate = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    #print(u"in系统启动时间: %s" % sysOpenDate )

    # 查看cpu逻辑个数的信息
    cpuLineCity = psutil.cpu_count()
    #print(u"CPU逻辑个数: %s" % cpuLineCity)

    # 查看cpu物理个数的信息
    cpuCore = psutil.cpu_count(logical=False)
    #print(u"CPU物理个数: %s" % cpuCore)

    #CPU的使用率
    cpuPer = (str(psutil.cpu_percent(1)))+"%"
    #print(u"cup使用率: %s" % cpuPer)
     
    #查看内存信息,剩余内存.free  总共.total
    #round()函数方法为返回浮点数x的四舍五入值。
 
    remainStorage = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2))+"G"
    allStorage = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2))+"G"
    memory = int(psutil.virtual_memory().total - psutil.virtual_memory().free) / float(psutil.virtual_memory().total)
    perStorage = str(int(memory * 100))+"%"

    #print(u"in物理内存： %s G" % allStorage)
    #print(u"in剩余物理内存： %s G" % remainStorage)
    #print(u"in物理内存使用率： %s %%" % perStorage )
    
    io = psutil.disk_partitions()
    #总硬盘大小
    allRam = ''
    #已使用硬盘大小
    sendRam =0
    #剩余硬盘大小
    remainRam = 0
    perRam =''
    perRams =''
    state = 0
    allRams = ''
    l = ""
    for i in io:
        #获取当前电脑硬盘信息
        o = psutil.disk_usage(i.device)
        #分区硬盘大小
        sizeRam = str(int(o.total / (1024.0 * 1024.0 * 1024.0)))+"G"
        #分区硬盘使用大小
        sendSizeRam = str(int(o.used / (1024.0 * 1024.0 * 1024.0)))
        #分区硬盘剩余大小
        remainSizeRam = str(int(o.free / (1024.0 * 1024.0 * 1024.0)))
        #print(u"in硬盘总大小： %s G" % sizeRam)
        #print(u"in硬盘使用大小：%s G" %sendSizeRam)
        #print(u"in硬盘剩余大小： %s G" %remainSizeRam)
        #print(o)
        #print(type(sizeRam),type(allRam))
        #print(int(sendSizeRam))
        #print(int(sizeRam))
        l =  str(o.percent)+"%"
        if state == 0:
            if o.percent < 80:
                state = 0
            else:
                state = 1
        perRams += l +"|"   
        allRams += sizeRam+"|"
    perRam  = perRams[:-1]
    allRam = allRams[:-1]

   # 各分区硬盘大小
    #print(allRam)
   # 个分区使用情况 
    #print(perRam)

    #perRam = allRam/sendRam
    #print(u"in硬盘总大小： %s G" % allRam)
    #print(u"in硬盘使用大小：%s G" %sendRam)
    #print(u"in硬盘剩余大小： %s G" %remainRam)
    #print(u"in硬盘大小使用率：%s %%" %perRam)
    
    
    db = pymysql.connect(host='122.224.131.235',user='root', password='123456', port=9092,database='psutil')
    cursor = db.cursor()
    
    # SQL 插入语句
    #先判断是否有这台机器没有添加否则更新
    sql = "select * from psutilmodel_psutil where ip = '%s'" % ip
    #print(sql)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data:
        sql_update = "UPDATE  psutilmodel_psutil SET sysDate= '%s' , sysOpenDate = '%s', cpuLineCity = '%s',cpuCore = '%s', cpuPer ='%s', allRam = '%s',remainRam = '%s',perRam = '%s',allStorage = '%s',remainStorage = '%s',perStorage = '%s',state = '%s'" % (sysDate,sysOpenDate,cpuLineCity,cpuCore,cpuPer,allRam,remainRam,perRam,allStorage,remainStorage,perStorage,state)+"where ip = '%s'" % ip
        #print(sql_update)
        try:
           # 执行sql语句
           cursor.execute(sql_update)
           # 提交到数据库执行
           db.commit()
           print('updateSucces')

        except Exception, e:
           # 发生错误时回滚
           print e
           db.rollback()
    else:
       sql_insert = "INSERT INTO psutilmodel_psutil (ip, sysDate,sysOpenDate,cpuLineCity,cpuCore,cpuPer,allRam,remainRam,perRam,allStorage,remainStorage,perStorage,state) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(ip,sysDate,sysOpenDate,cpuLineCity,cpuCore,cpuPer,allRam,remainRam,perRam,allStorage,remainStorage,perStorage,state)
       #print(sql)
       try:
           # 执行sql语句
           cursor.execute(sql_insert)
           # 提交到数据库执行
           db.commit()
           print('INSERTsucces')
       except Exception, e:
           # 发生错误时回滚
           print e
           db.rollback()
#每多少分钟执行一次

schedule.every(0.1).minutes.do(inspectionJob)
while True:
    schedule.run_pending()
    time.sleep(0)
  



