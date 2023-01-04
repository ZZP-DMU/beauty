from itertools import count
from operator import mod
import requests
from bs4 import BeautifulSoup
import os

src = 'http://jdlingyu.com/tuji/page/'
path = '/home/ZZP/workspace/temp/beauty/'
#the img file name 
count = 0

os.system('rm -rf /home/ZZP/workspace/temp/beauty/*')

src_list = []
html_list = []


for i in range(10):
    i = i+1
    src_list.append(src+str(i))

def get_html(src):
    r = requests.get(src,timeout=30)

    if r.status_code == 200:
        html = r.text
        print('from '+src+' get html successfully')
    else:
        print('from '+src+' get html failed')

    soup =  BeautifulSoup(html,'html.parser')

    link = soup.find_all('a')

    for i in link:
        u = i.get('href')
        if type(u) == type(''):
            flag = 'html' in u
            if flag:
                html_list.append(u)


def get_img(src):
    #the img src in one html
    img_src = []

    #the img file name
    global count

    r = requests.get(src,timeout=30)

    if r.status_code == 200:
        html = r.text
        print('from '+src+' get html successfully')
    else:
        print('form '+src+' get html failed')

    
    soup = BeautifulSoup(html,'html.parser')

    link = soup.find_all('img')

    for i in link:
        u = i.get('src')
        if type(u) == type(''):
            flag = 'webp' in u
            if flag:
                img_src.append(u)

    for i in img_src:
        pic = requests.get(i,timeout=30)

        f = open(path+str(count),mode='wb')
        print('write '+path+str(count)+' successfully')
        f.write(pic.content)
        f.close()
        count = count+1







for i in src_list:
    get_html(i)

for i in html_list:
    get_img(i)
