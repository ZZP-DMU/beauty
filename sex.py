import os
import requests
from bs4 import BeautifulSoup

os.system('rm -rf /home/ZZP/workspace/temp/sex/*')

src = 'http://www.sosi55.com/guochantaotu/list_22_'
src_base = 'http://www.sosi55.com'
src_list = []
html_list = []
path = '/home/ZZP/workspace/temp/sex/'
count = 0

for i in range(30):
    i = i+1
    src_list.append(src+str(i)+'.html')

def get_html(src):
    r = requests.get(src,timeout=30)

    if r.status_code == 200:
        html = r.text
        print('from '+src+' get html successfully')
    else:
        print('from '+src+' get html failed')

    soup = BeautifulSoup(html,'html.parser')

    link = soup.find_all('a')

    for i in link:
        u = i.get('href')
        if type(u) == type(''):
            flag = ('html' in u)and('2022' in u)and('#down_comment' not in u)
            if flag:
                html_list.append(src_base+u)

def get_img(src):
    global count

    img_list = []
    r = requests.get(src,timeout=30)

    if r.status_code == 200:
        html = r.text
        print('get in '+src+' successfully')
    else:
        print('get in '+src+' failed')

    soup = BeautifulSoup(html,'html.parser')

    link = soup.find_all('img')
    
    for i in link:
        u = i.get('src')
        if type(u) == type(''):
            flag = ('uploads/allimg' in u)and('jpg' in u)and('-L' not in u)
            if flag:
                img_list.append(src_base+u)
    
    for i in img_list:
        pic = requests.get(i)
        if pic.status_code == 200:
            print('get '+path+str(count)+' successfully')
            f = open(path+str(count),mode='wb')
            f.write(pic.content)
            f.close()
            count = count+1
        else:
            print('get '+path+str(count)+' failed')
    


for i in src_list:
    get_html(i)
for i in html_list:
    get_img(i)
