import requests

def py():
    url = 'http://fanyi.baidu.com/v2transapi'
    content="When in the group, he will stand slightly away so as to appear alone. Do you see him adjusting his tie, or making exaggerated movements or gestures? This means he is trying to stand out of the crowd. He wants to attract your attention towards him. He wants you to notice him like he has been noticing you."
    data={
        'from':'en','to':'zh',
        'query':content, 
        'transtype':'translang',
        'simple_means_flag':'3',
    }
    
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'}
    response = requests.post(url,data,headers=headers)
    print(response.text)

if __name__=="__main__":
    py()