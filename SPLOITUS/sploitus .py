import requests

banner='''

   .dMMMb  dMMMMb  dMP    .aMMMb  dMP dMMMMMMP dMP dMP .dMMMb 
  dMP" VP dMP.dMP dMP    dMP"dMP amr    dMP   dMP dMP dMP" VP 
  VMMMb  dMMMMP" dMP    dMP dMP dMP    dMP   dMP dMP  VMMMb   
dP .dMP dMP     dMP    dMP.aMP dMP    dMP   dMP.aMP dP .dMP   
VMMMP" dMP     dMMMMMP VMMMP" dMP    dMP    VMMMP"  VMMMP" 
'''
print(banner)
print('')
print('author:Nine world')
print('--------------------------------------------------------------------------------------')
def sploitus():
    #headers={'user-agent':'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36','content-type': 'application/json','accept': 'application/json','referer': 'https://sploitus.com/?query=MS17-010'}
    print('[!] Please select type')
    print('exploits')
    print('tools')
    xz=input('type:')
    user=input('query:')
    print('')
    headers={
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    url='https://sploitus.com/search'
    data={'offset':0,'query':"{}".format(user),'sort':"default",'title':'false','type':"{}".format(xz)}
    cookie={'__cfduid':'d7ecd3f6052b48a13d4a47e83dbdd15eb1536914053'}
    requt=requests.post(url=url,headers=headers,json=data,cookies=cookie)
    jds=requt.json()
    lp=jds['exploits'][0:]
    for l in lp:
        print('title:',l['title'])
        #print('published',l['published'])
        print('id',l['id'])
        print('type:',l['type'])
        print('url:',l['href'])
        print('')
sploitus()