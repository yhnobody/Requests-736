# -*-coding:utf-8 -*-
import requests

def download_image():
    """
    demo: 下载图片
    :return:
    """
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531198181794&di=4841f23d2cc184afee68c5f4464edaa3&imgtype=0&src=http%3A%2F%2Fpic002.cnblogs.com%2Fimages%2F2012%2F427440%2F2012071822433059.jpg"
    response = requests.get(url, headers=headers, stream=True)
    print(response.status_code, response.reason)
    print(response.headers)
    print(response.content)
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)

def download_image_improved():
    """
    demo:下载图片
    :return:
    """
    # 伪造headers信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531198181794&di=4841f23d2cc184afee68c5f4464edaa3&imgtype=0&src=http%3A%2F%2Fpic002.cnblogs.com%2Fimages%2F2012%2F427440%2F2012071822433059.jpg"
    #response = requests.get(url, headers=headers, stream=True)
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open('demo1.jpg', 'wb') as fd:
            # 每128字节写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


if __name__=="__main__":
    download_image_improved()