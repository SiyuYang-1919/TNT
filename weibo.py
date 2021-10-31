# import modules
import pprint
import requests as req
from lxml import etree

# Define url and get all the data
weiboid = input('weiboid:')
Cookie = input('Cookie:')

base_url = 'https://m.weibo.cn/comments/hotflow?id={weiboid}&mid={weiboid}&max_id_type={max_id_type}'
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

for comment in comments_data:
    text = comment['text']
    user_name = comment['more_info_users'][0]['screen_name']
    user_gender = comment['user']['gender']
    user_des = comment['user']['description']
    line = text+', '+user_name+', '+user_gender+', '+user_des+', '
    print(line)
print('Finish!')
