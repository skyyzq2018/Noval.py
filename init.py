#coding:utf-8
#noval_dn.py

def init(url):
    global d
    fp=open('noval.ini','r',encoding='utf-8')
    line = fp.readlines()
    #print(line)
    loops=(1+len(line))//5
    #print(len(line),loops)

    fp.close()
    www={}
    d={}

    def https():
        #网站
        d={}
        ll=fp.readline().strip().split(' ')
        name=ll[0]
        d['name']=name
        ww=ll[1]
        d['url']=ll[1]
        ll=fp.readline().strip()
        ll=ll[3:]
        
        ll=ll.split('=')
        if ll[0]=='class':
            d['intro']={'class_':ll[1][1:-1]}
        else:
            d['intro']={'id':ll[1][1:-1]}

        ll=fp.readline().strip()
        ll=ll[3:]
        ll=ll.split('=')
        if ll[0]=='class':
            d['mulu']={'class_':ll[1][1:-1]}
        else:
            d['mulu']={'id':ll[1][1:-1]}
            
        ll=fp.readline().strip()
        ll=ll[3:]
        ll=ll.split('=')
        if ll[0]=='class':
            d['chapter']={'class_':ll[1][1:-1]}
        else:
            d['chapter']={'id':ll[1][1:-1]}

        www[ww]=d
        #print(d)
        fp.readline()
        

  
    fp = open('noval.ini','r',encoding='utf-8')
    for i in range(loops):
        https()

    #print(www)

    fp.close()

    root=url[:url[8:].find('/')+9]
    key=''
    for k in www.keys():
        if www[k]['url']==root:
            key=k
            #print(key)

    ###
    if key=="":
        return None,None,None,None
        
    root=www[key]['url']
    intro = www[key]['intro']
    mulu=www[key]['mulu']
    chapter=www[key]['chapter']
    ###
    return root,intro,mulu,chapter

if __name__ == '__main__':
    url='https://www.ibooktxt.com/41_41406/'
    print(init(url))
    #print(www)
    
