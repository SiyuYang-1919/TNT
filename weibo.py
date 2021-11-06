# import modules
import pprint
import requests as req
from lxml import etree

# Define url and get all the data
# weiboid = input('weiboid:')
# Cookie = input('Cookie:')
weiboid = '4699558267589769'
Cookie = 'WEIBOCN_FROM=1110106030; SUB=_2A25MgkhZDeRhGeNJ6loQ8inKyD2IHXVvjWgRrDV6PUJbktCOLRjgkW1NS_qc_o79TJa-bggNL-0lZIVTHQyXZYxV; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWnwqUV4xcD.cyO7G8BGCdn5NHD95QfS02ReKzNSoepWs4Dqcj.i--RiK.piKLFi--ciK.4iK.0i--ciK.4iK.0i--fi-88iKnp; SSOLoginState=1636186122; _T_WM=30376273205; XSRF-TOKEN=fa0b2a; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4699558267589769%26luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E6%259C%25B1%25E9%259B%2580%25E8%2588%259E%25E5%258F%25B0'


base_url = 'https://m.weibo.cn/comments/hotflow?id={weiboid}&mid={weiboid}&max_id={max_id}&ax_id_type={max_id_type}'
headers = {
    'Cookie' : 'WEIBOCN_FROM=1110006030; SUB=_2A25MeRsFDeRhGeVM7loR-CrEyzyIHXVvhaVNrDV6PUJbkdCOLXTskW1NTNbxOYs4lZBoeGkr0w6ZFJfikVXUvtwd; _T_WM=72881388523; MLOGIN=1; XSRF-TOKEN=6a5436; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D3%2526q%253Dtnt%2526t%253D0%26oid%3D4698146842086851%26uicode%3D10000011%26fid%3D1076036624589897',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
}
user_url = 'http://weibo.cn/{uid}/info'

url = 'http://m.weibo.cn/comments/hotflow?id={weiboid}&mid={weiboid}&max_id_type=0'.format(weiboid=weiboid)
response = req.get(url, headers=headers, timeout=10)
data = response.json()

# Filter information that we want
comments = data.get('data')
comments_data = comments['data']
rows = []

comment = comments_data[0]

time = comment['created_at']
text = comment['text']
user_id = comment['user']['id']
user_name = comment['user']['screen_name']
user_gender = comment['user']['gender']
user_des = comment['user']['description']
# Other information
url2 = user_url.format(uid=user_id)
user_info = req.get(url2, headers=headers)
user_info.encoding = 'utf-8'
root = etree.HTML(user_info.content)
user_location = root.xpath("/html/body/div[6]/text()[4]")
user_birth = root.xpath("/html/body/div[6]/text()[5]")
user_other = root.xpath("/html/body/div[6]/text()[6]")

print(user_info)