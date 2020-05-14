
import requests
url = 'https://www.baidu.com/'                 # 创建需要爬取网页的地址
# 创建头部信息
headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 6.1;W…) Gecko/20100101 Firefox/59.0'}
response = requests.get(url, headers=headers)        # 发送网络请求
print(response.content)
