#!/usr/bin/env python
# coding=utf-8
import os
import re
import Queue
from threading import Thread
import time
import requests
import telnetlib
import json
from bs4 import BeautifulSoup



class mainThread(Thread):
    TIMEOUT = 5

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            url = self.queue.get()
            try:
                data = self.telnetrequest(url)
            except:
                continue
    def telnetrequest(self,url):
        host = url.split(":")[0]
        port  = url.split(":")[-1]
        try:
            tn = telnetlib.Telnet(host, port=port, timeout=self.TIMEOUT)  
            tn.set_debuglevel(3)
            print '[+]'+url+'--ok'
            #datas.append(url)
            self.loglog(url)
        except Exception, e:
            print '[?]'+url+'--'+str(e)
        finally:
            tn.close()
    def loglog(self,data):
        self.file_object = open('ok.txt','a')
        try:
                self.wdata = data+'\n'
                self.file_object.write(self.wdata)
        finally:
            self.file_object.close( )        
if __name__ == '__main__':
    iplist = []
    file_object = open("ip.txt",'r')
    try:
        lines = file_object.readlines()
        for line in lines:
            iplist.append(line.strip('\n'))
    finally:
        file_object.close()    
 
    datas = []
    queue = Queue.Queue()
    for ip in iplist:
        for port in range(8000,11000):
            url = str(ip)+':'+str(port)
            queue.put(url)         
  
    print u'利用telnet扫描服务器开放的端口'
    print "----------------------------------------------------------------"
    print u'队列大小: '+str(queue.qsize())
    threadl = []
    threads = 500
    threadl = [mainThread(queue) for x in xrange(0, threads)]
    for t in threadl:
        t.start()
        #print '[+]'+t.name+' start'
    for t in threadl:
        t.join()