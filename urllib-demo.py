# _author_: nobody DATA : 2018/7/5 14:01 FILE_NAME : .py IDE_NAME : PyCharm

# -*- coding:utf-8 -*-

from urllib.request import urlopen
from urllib import request
from urllib import parse

URL_IP = "http://httpbin.org/ip"
#URL_IP = "https://www.baidu.com"
URL_GET = "http://httpbin.org/get"

def use_simple_urllib():
    response = urlopen(URL_IP)
    print('>>>>Response Headers:')
    print(response.info())
    print(">>>>Response Body:")
    print(response.read().decode('utf-8'))

def use_params_urllib():
    params = parse.urlencode({'param1':'hello', 'param2':'world'})
    print('Request Params:')
    print(params)
    response = urlopen('?'.join([URL_GET, "%s"]) % params)
    print('>>>>Response Headers:')
    print(response.info())
    print('Status Code:')
    print(response.getcode())
    print(">>>>Response Body:")
    print(response.read().decode('utf-8'))


if __name__=='__main__':
    #print('>>>Use simple urllib:')
    #use_simple_urllib()
    print('>>>Use params urllib:')
    use_params_urllib()
