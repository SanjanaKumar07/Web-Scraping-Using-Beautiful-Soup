from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

html = urlopen('https://www.commandonetworks.com/switches/SF50-5')
bs = BeautifulSoup(html.read(),'lxml')

#images
img_tags = bs.find_all("img",{"class" : "product-v-img"})
count = 0
for i in img_tags:
        #print(i['src'])
        try:
            #passing image urls one by one and downloading
            urllib.request.urlretrieve(i['src'], str(count)+".jpg")
            count+=1
            print("Number of images downloaded = "+str(count),end='\r')
        except Exception as e:
            pass


#info
name=bs.find("h2",{"class":"post-title"})
print(name.get_text())
description =bs.find("div",{"class":"block-devider"})
print(description.get_text())
info =bs.find("div",{"class":"page-section hero"},{"id":"info"})
print(info.get_text())
specification =bs.findAll("tr")
for tag in specification:
    print(tag.get_text())