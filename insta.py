#!D:/Python3/python.exe
import cgi
import re
import urllib,urllib.request
import time
import os
import _thread
import threading
import datetime
#os.environ['NO_PROXY'] = 'instagram.com'

form = cgi.FieldStorage() # парсинг данных формы
l=threading.Lock()#создаём блокировку

'''def loadF(newurl,photoname):
    try:
        urllib.request.urlretrieve(newurl, 'C://Server/www/'+photoname+'.jpg')
    except Exception as err:
        print("Wrong link")
'''        
def Uol():
    try:
        with l:
            link = str(urllib.request.urlopen(cgi.escape(form['link'].value)).read())
            ex=re.compile(r'(("display_url"|"video_url"):"https://(.*?).(jpg|mp4)")')
            result=ex.finditer(link)
            photos=[]
            for ma in result:
                if str(ma.group(0)) not in photos:
                    photos.append(str(ma.group(0)))
            if len(photos)==0:
                 print("<div align=\"center\">")
                 print("<h1>Wrong link</h1>")
                 print("</div>")
            delsize=0
            typecontent=""
            for newurl in list(photos):
                if "video" in newurl:
                    delsize=13
                    typecontent="<div id=\"cont\" align=\"center\"><video controls=\"controls\"><source src=\"$URL$\"></video></div>"
	
                else:
                    delsize=15
                    typecontent="<div id=\"cont\" align=\"center\"><img src=\"$URL$\" alt=\"альтернативный текст\"> </div>"
                   
                newurl=newurl[delsize:len(newurl)-1]
                print(typecontent.replace("$URL$",newurl))
    except Exception as er:
        print(er)
    now=str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
    print("<footer>")
    print("<p>Правой нопкой мышки кликните на фотографию или видео и выберите пункт \"Сохранить изображение(видео) как...\"</p>")
    print("</footer>")
    print("<div id=\"dt\" align=\"center\">"+now+"</div>")
    print("</div>")
    print("</body>")
    print("</html>")    

def htmlS():
    print('Content-type: text/html\n')
    with open("InstagramLo.html") as file:
        for i in range(0,25):
            print(file.readline(),end="\n")
            
htmlS()
	
if not 'link' in form:
    print("<div align=\"center\">")
    print("<h1>Empty</h1>")
    print("</div>")
else:
    thread = threading.Thread(target=Uol, args=())
    thread.start()
    thread.join()
  
  

