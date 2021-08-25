import requests
from bs4 import BeautifulSoup
import urllib.request


opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

url = "https://stockcharts.com/h-sc/ui?s=spy"
req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()

soup = BeautifulSoup(res,'html.parser')
soup = soup.find("div", class_ ="chartImg")
imgUrl = soup.find("img")["src"]

print (imgUrl)

#urlretrieve는 다운로드 함수
#img.alt는 이미지 대체 텍스트 == 마약왕
#urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"]+'.jpg')

#opener = urllib.request.build_opener()
#opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
#urllib.request.install_opener(opener)
#urllib.request.urlretrieve(imgUrl, 'spy' + ".jpg")