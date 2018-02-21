# Author: Jason Lu


pattern1 = '<div id="plist".+?<div class="page clearfix">'
pattern2_jpg = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg)">'
pattern2_png = '<img width="220" height="220" data-img="1" src="//(.+?\.png)">'

pattern3_jpg = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)"'
pattern4 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.png)"'

import urllib.request
import urllib.error
import re
import types

def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    result1 = re.compile(pattern1).findall(html1)
    result1 = result1[0]
    imagelist1_jpg = re.compile(pattern2_jpg).findall(result1)
    imagelist1_png = re.compile(pattern2_png).findall(result1)
    imagelist3_jpg = re.compile(pattern3_jpg).findall(result1)
    # imagelist4 = re.compile(pattern5).findall(result1)

    imagelist = imagelist1_jpg+imagelist3_jpg# + imagelist2# + imagelist3 + imagelist4
    print(len(imagelist))
    x = 1
    for imageurl in imagelist:
        print("{},{}".format(imageurl, type(imageurl)))
        if imageurl.endswith(tuple(["jpg"])):
            imagename = "img_jd/"+str(page)+str(x)+".jpg"
        elif imageurl.endswith(tuple(["png"])):
            imagename = "img_jd/"+str(page)+str(x)+".png"
        else:
            continue

        imageurl = "http://"+imageurl
        print("{},{}".format(imageurl, imagename))
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                print(e.code)
                x += 1
            if hasattr(e, 'reason'):
                print(e.reason)
                x += 1
        x += 1



for i in range(1, 2):
    url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url, i)






