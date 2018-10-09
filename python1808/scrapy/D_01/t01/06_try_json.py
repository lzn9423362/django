import json

import requests



url = 'https://fanyi.baidu.com/multitransapi'


data = {'from': 'zh',
'to': 'en',
'query': '我在天上飞',
}



headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# response = requests.post(url, data=query_string, headers=headers)

response = requests.post(url, data=data, headers=headers)

# with open('index.html', 'a', encoding='utf-8') as f:
#     f.write(response.content.decode())


result = response.content.decode()

dict_res = response.json()

res = dict_res['data']['cands'][0]
# print(res)

print(result)