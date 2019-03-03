# encoding: UTF-8
import urllib2
import re
import socket
 
rfile = open('ip.txt')
wfile = open('result.csv', 'w+')
for line in rfile:
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux 5.5; rv:6.0.2) Gecko/20120101 Firefox/9.0.0')]
    req = opener.open('http://www.ip-adress.com/reverse_ip/'+line.strip())
    responseHtml = req.read()
    match = re.findall(r'<td>/r/n(.+)</td>', responseHtml)
    wfile.write(socket.gethostbyname(line.strip())+',')
    print line.strip()
    for val in match:
        wfile.write(val+',')
    wfile.write('/n')
rfile.close()
wfile.close()
 