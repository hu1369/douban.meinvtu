import json
import random
import urllib
from urllib import error
from urllib import request
import requests
from bs4 import BeautifulSoup

# 得到网站首页图片的子网页
def get_html(url):
    index_list = []
    header = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    , {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}]
    for i in url:
        try:
            req = urllib.request.Request(i, headers=random.choice(header))
            response = urllib.request.urlopen(req, timeout=50)
            html = response.read()
            list = BeautifulSoup(html,'lxml')
            for i in list.find_all('a',class_='TypeBigPics'):
                index_list.append(i['href'])
        except urllib.error.URLError as e:
            print(e.reason)

    return index_list



# 获取子页面的图片
def get_imgs(index_list):
    imgs = []
    for i in index_list:
        header = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
            , {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}]
        for j in range(1,3):
            if j == 1:
                pass
            elif j == 2:
                i = i[0:-5]+'_'+ str(j+2) +'.html'
            try:
                req = urllib.request.Request(url=i, headers=random.choice(header))
                response = urllib.request.urlopen(req, timeout=50)
                html = response.read()
                list = BeautifulSoup(html, 'lxml')
                for item in list.select('body > div.content > img'):
                    imgs.append(item['src'])
            except urllib.error.URLError as e:
                print(e.reason)
    return imgs


#设定下载到多少页
def getnum(num1,num2):
    url = 'https://www.ku66.net/r/1/list_1_1.html'
    list= []
    for i in range(num1,num2+1):
        list.append(url[0:-6] +str(i) +'.html')
    return list

#下载图片
def download_imgs(imgs):
    count = 0
    for i in imgs:
        try:
            count += 1
            print('第' + str(count) + '张图片开始下载')
            print('---------------------------------------------------------')
            print('第' + str(count) + '张图片完成下载')
            urllib.request.urlretrieve(i, './妹妹图/' + str(count) + '.jpg')
        except:
            print('wrong')



if __name__ == '__main__':
    # 设置下载到多少页
    num = getnum(353,355)
    index_list = get_html(num)
    imgs = get_imgs(index_list)
    download_imgs(imgs)