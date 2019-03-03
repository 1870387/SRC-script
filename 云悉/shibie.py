import requests
import threading
import re

def zhuaqu(urls):
    user=input('url:')
    data={}
    data2={}
    headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url2='http://www.yunsee.cn/home/getInfo'
    reqts=requests.get(url=urls,headers=headers)
    search=re.search('_token:.*',reqts.text)
    token='{}'.format(search.group()).replace('}','').replace(',','').replace('"','').replace(':','').replace('_token','').strip()
    datas='type=webcms&url={}&_token={}'.format(user,token)
    datas2 = 'type=webinfo&url={}&_token={}'.format(user, token)
    for v in datas.split('&'):
        key,value=v.split('=',1)
        data[key]=value

    reqvs=requests.post(url=url2,headers=headers,data=data)
    jsons=reqvs.json()

    for v in datas2.split('&'):
        key, value = v.split('=', 1)
        data2[key] = value

    reqvs2 = requests.post(url=url2, headers=headers, data=data2)
    json2=reqvs2.json()

    print('url:{}'.format(user))
    print('url:{}'.format(user),file=open('save.txt','a'))    
    print('whois_dns:{}'.format(json2['res']['whois_dns']))
    print('icp_name:{}'.format(json2['res']['icp_name']))
    print('ip:{}'.format(json2['res']['ip']))
    print('language:{}'.format(json2['res']['language']))
    print('whois_mail:{}'.format(json2['res']['whois_mail']))
    print('os:{}'.format(json2['res']['os']))
    print('cdn:{}'.format(json2['res']['cdn']))
    print('server:{}'.format(json2['res']['server']))
    print('record_id:{}'.format(json2['res']['record_id']))
    print('whois_isp:{}'.format(json2['res']['whois_isp']))
    #print('LLC:{}'.format(json2['res']['LLC']))
    print('whois_date:{}'.format(json2['res']['whois_date']))
    print('create:{}'.format(json2['res']['create']))
    print('icp_id:{}'.format(json2['res']['icp_id']))
    print('whois_name:{}'.format(json2['res']['whois_name']))
    print('idc:{}'.format(json2['res']['idc']))

    print('cms:{}'.format(jsons['mess']))
    for reqs in jsons['res'][0:]:
        print('desc:{} name:{}'.format(reqs['desc'],reqs['name']))
def run():
    url = 'http://www.yunsee.cn/'
    t=threading.Thread(target=zhuaqu,args=(url,))
    t.start()
if __name__ == '__main__':
    run()