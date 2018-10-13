import requests
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.cn/Attractions-g297407-Activities-Xiamen_Fujian.html'

wb_data = requests.get(url)

soup = BeautifulSoup(wb_data.text, 'lxml')

# print(soup)

titles = soup.select('.photo_image')
cates = soup.select('.matchedTag')
print(titles, cates)

