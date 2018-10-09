import requests
from retrying import retry
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

}
#让被装饰的函数反复执行三次，三次全部报错才会报错
@retry(stop_max_attempt_number=3)
def _parse_url(url):
    response = requests.get(url, headers=headers, timeout=5)#5秒内必须返回参数否则会报错
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    # url = 'www.baidu.com'
    print(parse_url(url))