import time
start = time.time()

xj=open('ip.txt','w')
xj.close()

print('[+]Emptying IP.txt')
def sc():
    user=input('Please enter IP, similar to 127.0.0.:')
    for x in range(1,256):
        a = '{}{}'.format(user,x)
        print(a,file=open('ip.txt','a'))
sc()
stop=time.time()
print('[+]time consuming {}'.format(start-stop))