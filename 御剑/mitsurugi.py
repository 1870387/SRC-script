import requests
import random
import os
file=[]
url=[]
error=[]
bc=[]
ip=[]
headers={}
user=input('Import TXT:')
banner='''
 ____            _                             
|  _ \  ___  ___| |_ _ __ ___  _   _  ___ _ __ 
| | | |/ _ \/ __| __| '__/ _ \| | | |/ _ \ '__|
| |_| |  __/\__ \ |_| | | (_) | |_| |  __/ |   
|____/ \___||___/\__|_|  \___/ \__, |\___|_|   
                               |___/        

Producer:Nine world 
'''
useragent=[]
twoo=[]
print(banner)

def urls():
    dk=open('{}'.format(user),'r')
    for k in dk.readlines():
        qcs="".join(k.split('\n'))
        url.append(qcs)
    print('[+]url.txt Load completion')
    print(' ')
    print(' ')
urls()

def judge():
  pd=os.listdir('御剑配置文件')
  for name in pd:
      file.append(name)

  for f in file:
    print('[+]existence {}'.format(f))

  print(' ')
  print(' ')

  dk=open('user-agent.txt','r')
  for d in dk.readlines():
      qc="".join(d.split('\n'))
      useragent.append(qc)
  print('[+]user-agent Load completion')
  print(' ')
  print(' ')
judge()

def errors():
    lv=open('Error/error.txt','r',encoding='utf-8')
    for e in lv.readlines():
        qcsw="".join(e.split('\n'))
        error.append(qcsw)
    print('[+]The filter file is loaded')
    print(' ')
    print(' ')
errors()

def forge():
    sj=[]
    dkw=open('ip.txt','r')
    for i in dkw.readlines():
        k="".join(i.split('\n'))
        ip.append(k)

    for g in range(0,len(useragent)):
        u='User-Agent='
        x='X-Forwarded-For='
        c='Client-IP='
        sj.append(u+useragent[g]+'&'+x+ip[g]+'&'+c+ip[g])
    kc=list(set(sj))
    su=random.choice(kc)
    qc=str(su)
    for v in qc.split('&'):
        key,value=v.split('=',1)
        headers[key]=value
forge()

def exploit():
  wi=os.listdir('御剑配置文件')
  for w in wi:
      dp=open('{}'.format('御剑配置文件/'+w),'r',encoding='gbk')
      for s in dp.readlines():
          we="".join(s.split('\n'))
          for u in url:
              up='{}'.format(u).rstrip('/')+we
              try:
                requet=requests.get(url=up,headers=headers,timeout=3,allow_redirects=False)
                for e in error:
                    if requet.status_code==200 and not e in requet.text:
                        ok='[+]code:{} url:{}'.format(requet.status_code,requet.url)
                        if ok in twoo:continue
                        twoo.append(ok)
                        print(ok)
                    else:
                        no='[x]Not url :{}'.format(requet.url)
                        if no in bc:continue
                        bc.append(no)
                        print(no)
              except Exception as u:
                  print('[-]Error {}'.format(u))

  if len(twoo)>0:
      od=open('save.txt','w')
      od.close()

      xr=open('save.txt','r')
      for c in twoo:
          print(c,file=open('save.txt','a'))


exploit()
