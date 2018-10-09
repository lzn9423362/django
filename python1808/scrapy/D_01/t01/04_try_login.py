import requests

url = 'https://www.renren.com'
headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

cookie = 'anonymid=jmzrl81b-yhg5lg; depovince=GW; _r01_=1; ick_login=923eed27-e474-4beb-9304-25c52da54924; jebe_key=2fa07ce0-e5d5-42c6-b54c-a7ba234b853e%7Ccfcd208495d565ef66e7dff9f98764da%7C1538970986314%7C0%7C1538970985476; jebecookies=bc18d987-f08a-43cb-b06f-1e685805be83|||||'

cookie_dict = {i.split('=')[0]: i.split('=')[-1] for i in cookie.split('; ')}

response = requests.get(url=url, headers=headers)

with open('renren.html', 'w') as f:
    f.write(response.content.decode())