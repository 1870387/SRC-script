#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import threading
import queue
import sys,getopt

Number_threads=10#默认的线程
out_file='res.txt.txt'#默认保存的文件
error=20  #误差值（5~10），此参数不用修改,已最优。

help="""
python3 解释漏洞批量扫描器V1.0,准确率高，报错请认真检查当前是否为python3。
-t   指定线程数（默认 10）
-f   待扫描的域名文件
-o   保存的名字
使用例子：
python3 *.py -t 10 -f url.txt -o res.txt
"""
if len(sys.argv)<2:
    print(help)
    sys.exit()
try:
    opts, args = getopt.getopt(sys.argv[1:], "t:f:o:h", ["b="])
    for opt, arg in opts:
        if "-t" == opt:
            Number_threads=int(arg)
        elif '-f' == opt:
            filr_=arg
           # heavy=""
        elif '-o'==opt:
            out_file=str(arg)
        elif '-h' == opt:
            print (help)
            sys.exit(1)

except getopt.GetoptError as e:
    print ('参数解析发生了错误:' + e.msg)
    sys.exit(1)

def is_http(url):#判断url是否已存在http://,没有就自动加上
    if 'http://' in url or 'https://' in url:
        url_res=url
        pass
    else:
        url_res='http://'+url
    return url_res

def test(q):
    global error,out_file
    while not q.empty():
        url=q.get()
        try:
            path = '/robots.txt/.php'
            path2 = '/robots.txt/.232index'#异常测试时需要，能降低防止误报
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            res=requests.get(url=url+path,verify=False,timeout=5)
            count=len(res.text)
            if res.status_code==200:#判断响应值
                if 'ser-agent' in res.text or 'isallow' in res.text:#判断返回的内容
                    res2 = requests.get(url=url + path2, verify=False, timeout=5)
                    count2=len(res2.text)
                    sum=count-count2
                    if error>=abs(sum):#获取绝对值，计算误差。
                        print(url + path2 + ' No Loophole')
                    else:
                        print(url+' \033[1;35m   确定存在解释漏洞************************************************* \033[0m')
                        open(out_file, 'a', encoding='utf-8').write(url + path +'  '+' 存在解释漏洞' + '\n')#写入文件
                else:
                    print(url+' No Loophole')
        except Exception as e:
            print(url,str(e))
            pass
        q.task_done()
q=queue.Queue()
for i in open(filr_,'r',encoding='utf-8').read().split():
    q.put(is_http(i))

for i in range(Number_threads):#15个线程
    threading.Thread(target=test,args=(q,)).start()

q.join()#等待队列为空，结束程序
print('task complete~~~~~~~~~~ 完了')

