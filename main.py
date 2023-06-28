#coding：utf8
'''
noval.py

pip install requests bs4 lxml
pip curl_cffi

from curl_cffi import requests
res = requests.get(url='https://www.baidu.com/',impersonate="chrome101")
print(res.text)

'''
#import re
import requests
#from curl_cffi import requests
import sys
from bs4 import BeautifulSoup as bs
from random import randint
DELAY=randint(1,10)/100      #0.010 #每隔1秒下载一个网页。
#DELAY=3
argv=sys.argv
print(len(argv),argv,"\n\tDELAY=",DELAY)
del sys

head={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360EE'}
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
rootUrl={}
encode ='UTF-8'
chapter={}
mulu={}
root=''
twopage= False
url='https://www.qisuu.la/du/35/35199/'
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

if len(argv)<2:
    url=input("\n请输入小说网址:")
    
else:
    url=argv[1]
    
try:
    
    r = requests.get(url,headers=head,verify=False)
    #r = requests.get(url,impersonate="chrome101")

    print(r.encoding)
except:
    print("网址错误:"+url)
    input()
    quit()

twopage = input("两页？")

encode = r.apparent_encoding
#encode = r.charset
##if r.encoding != 'UTF-8':
##    #r.encoding="GBK"
##    r.encoding="UTF-8"
##    encode="UTF-8"
##    #r.charset='GBK'

from init import init

root,intro,mulu,chapter = init(url)

if root==None:
    print("再试。。。")
    _,intro,mulu,chapter = init('http://www.biqugse.com/')
    root=url[:url[8:].find('/')+9]
if root == None:
    print("再试2。。。")
    _,intro,mulu,chapter = init('https://www.biqvge8.com/')
    root=url[:url[8:].find('/')+9]
if root == None:
    print("再试3。。。")
    _,intro,mulu,chapter = init('https://www.biququ.info/')
    root=url[:url[8:].find('/')+9]

if root == None:
    print("再试4。。。")
    _,intro,mulu,chapter = init('http://www.bbzayy.com/')
    root=url[:url[8:].find('/')+9]

if root == None:
    print("请在 noval.ini 文件中标记网页特征")
    from sys import exit
    exit()
    quit()
        

print("根路径：",root)
u=''
a=''
h=''
    
def chp(a,page): #章节
        u=a['href']
        #print(u)
        ch=''
        try:
            if a['title'] !=None:
                ch=a['title']
        except:
            ch=a.text
                
            
        if u[:4]!='http':u=url+u;#print(u)
        try:
            r=requests.get(u,headers=head,verify=False)
            #r=requests.get(u,impersonate="chrome101")
        except:
            print("再试。。。")
            time.sleep(DELAY)
            #r=requests.get(u,impersonate="chrome101")
            r=requests.get(u,headers=head,verify=False)
            try:
                time.sleep(DELAY)
                #r=requests.get(u,impersonate="chrome101")
                r=requests.get(u,headers=head,verify=False)
            except:
                print("再试 2。。。")
                time.sleep(DELAY)
                #r=requests.get(u,impersonate="chrome101")
                r=requests.get(u,headers=head,verify=False)
##        r.encoding=encode
##        if r.encoding == 'GB2312':
##            r.encoding="GBK"

        #s=r.text
        s=r.content.decode(r.apparent_encoding)
        #s=r.content
        s=s.replace("<p>","<p>\n\t") #段落,美观,格式化便于阅读
        h=bs(s,'lxml')
        if len(s)>1000:
            txt=h.find(**chapter)
            try:
                txt='\n'+ch+"\n\t"+txt.text.strip()
            except:
                try:
                    print("再试 3。。。")
                    r=requests.get(u,impersonate="chrome101")
                    r.encoding=r.charset
                    if r.charset== 'GB2312':
                        r.encoding="GBK"
                    s=r.text
                    s=s.replace("<p>","<p>\n\t")
                    h=bs(s,'lxml')
                    txt=h.find(**chapter)
                    
                    if txt == None:
                        txt='\n'+ch+"\n\t"+"网页下载错误"
                    else:
                        txt='\n'+ch+"\n\t"+txt.text
                except:
                    txt='\n'+ch+"\n\t"+"网页下载错误"
        else:txt='\n'+ch+"\n\t"+"404 Not Found"
        
        txt=txt.replace('    ','\n\t')
        txt=txt.replace('　　','\n\t')
        txt=txt.replace('\r\n','\n')
        txt=txt.replace('\n\n','\n')
        txt=txt.replace('\n\n','\n')
        txt=txt.replace('&nbsp','')
        txt=txt.replace('\t\n','')
        txt=txt.replace('\r \r\n','\n')
        txt=txt.replace(r'chaptererror();','')
        fp.write(txt.encode('utf-8'))
        print(f"{novalName}[{jj:04d}: {page+1:04d}]\t{ch}")
        
        return txt

print(r.encoding)
#encode='GBK'
#r.encoding = encode
   
#s=r.text
s=r.content.decode(encode)

h=bs(s,'lxml')

#简介code

intros = h.find(**intro).text

name_code='h1'
if len(h.find_all('h1'))==0:
   name_code='h2'
   if len(h.find_all('h2'))==0:
       name_code={'id':'title'}

try:
    novalName=h.find_all(name_code)[-1].text.strip()
except:
    novalName=h.find_all(**name_code)[-1].text.strip()
    
if novalName.find(" ") != -1: novalName=novalName[:novalName.find(" ")]

#目录code
mulus=h.find_all(**mulu)

mulu_list=mulus[len(mulus)-1]
mulu_list=mulu_list.find_all('a')
from pathlib import Path
if not Path(r'./txt').is_dir():
    import os
    os.mkdir(r'./txt')
    del os
del Path

#fp=open("txt\\"+novalName+'.txt','w',encoding='gbk')

fp=open("txt/"+novalName+'.txt','wb')

print('\n\n\t\t《',novalName,"》\n网址:",url)
print("\n"+intros)

urls=mulu_list
maxlen=len(urls)
    
j,jj="",""
if len(argv)<2:
    j=input("\n\t起始页（总页数%d）:"%maxlen)
    jj=input("\n\t结束页（总页数%d）:"%maxlen)

if j=='':j=0
else:j=int(j)

if jj=='':jj=maxlen
else:jj=int(jj)

if len(argv)>=3:
    j=argv[2]
    j=int(j)
    print("="*30+'\n')
    print(j)
if len(argv)>=4:
    jj=argv[3]
    jj=int(jj)
    print(jj)
    

fp.write(novalName.encode('utf-8'))
s="\n"+f"网址： {url}\n"+intros
fp.write(s.encode('utf-8'))

if urls[j]['href'].find("/") ==-1:
    pass
else:
    url=root

if urls[j]['href'][0]=='/':
    url=url[:-1]

print(urls[j]['href'])


import time
#requests.adapters.DEFAULT_RETRIES = 5
for i in range(j,jj):
        chp(urls[i],i) #章节

        if not twopage=='':
            u=urls[i]['href']
            urls[i]['href']=u[:-5]+'_2'+u[-5:]
            #print(urls[i]['href'])
            chp(urls[i],i) #章节

        time.sleep(DELAY)

fp.close()
