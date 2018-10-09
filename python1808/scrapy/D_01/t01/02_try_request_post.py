import requests

url = 'https://fanyi.baidu.com/multitransapi'



data = {'from': 'zh',
'to': 'en',
'query': '彭性感真的是头猪',
}



headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# response = requests.post(url, data=query_string, headers=headers)

response = requests.post(url, data=data, headers=headers)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(response.content.decode())

print(response.encoding)

result = response.content.decode()

print(type(result))

print()