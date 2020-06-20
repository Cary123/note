import requests
from bs4 import BeautifulSoup
import codecs
f = codecs.open('../Resources/spider2.txt', 'w', 'utf8')
for i in range(5000, 5500):
    url = "http://www.xoxo111.com/vod-detail-id-"+str(i)+".html"
    res = requests.get(url)
    if res.status_code == 200:
        res.encoding = 'utf8'
        soup = BeautifulSoup(res.text, 'html.parser')
        lists = soup.select('h1')
        if len(lists) > 0:
            txt = lists[0].text
            f.writelines(url+"   :   "+txt +"\r\n")