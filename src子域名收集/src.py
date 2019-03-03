# -*- coding: utf8 -*-
import requests
import logging
from concurrent import futures

logging.basicConfig(level=logging.INFO, format="%(message)s")


class Src:
    def __init__(self, max_threads=50, max_timeout=3, url_file='url.txt'):
        self.max_threads = max_threads  # 最大并发线程数
        self.max_timeout = max_timeout  # 最大请求超时时间
        self.url_file = url_file        # 同级目录下存放爆破出来的域名的文件名

        self.executor = futures.ThreadPoolExecutor(max_workers=max_threads)

        self.headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
            'Referer': 'http://www.58.com/',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            # 'Cookie': '这里写你的Cookie',
            'Connection': 'close'
        }

    def auth(self, url):
        try:
            r = requests.get(url=url, headers=self.headers,
                             timeout=self.max_timeout)
            content = r.content
            if content:
                header_list = []  # ['nginx/1.10.3', 'PHP/5.6.20']
                header_server = r.headers.get('Server')
                header_XPoweredBy = r.headers.get('X-Powered-By')

                if header_XPoweredBy is not None:
                    header_list.append(header_XPoweredBy)
                if header_server is not None:
                    header_list.append(header_server)

                if not r.history:
                    logging.info(
                        "[ ] {} => {} => {}".format(url, r.status_code, header_list))
                else:
                    status_lst = []
                    for code in r.history:
                        status_lst.append(code.status_code)
                        status_lst.append(r.status_code)
                    logging.info(
                        "[+] {} => {} => {}".format(url, status_lst, header_list))
        except:
            pass

    def dispatcher(self):
        try:
            with open(self.url_file) as f:
                while True:
                    line = f.readline()
                    if line:
                        url = "http://" + line.strip()  # 去掉每行末尾的\r\n
                        self.executor.submit(self.auth, url)
                    else:
                        break
        except Exception:
            pass


if __name__ == '__main__':
    src58 = Src(max_threads=100, max_timeout=3, url_file='url.txt')
    src58.dispatcher()