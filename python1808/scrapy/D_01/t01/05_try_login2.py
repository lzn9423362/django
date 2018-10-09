import requests

url = 'https://www.renren.com'
headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
post_data = {'email':0, 'password':1}
session = requests.session()
session.post(url,headers=headers,data=post_data)
response = requests.get(url=url, headers=headers)

with open('renren.html', 'w') as f:
    f.write(response.content.decode())