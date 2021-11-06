# import modules
import pprint
import requests as req
from lxml import etree
from lxml import html
from html import unescape
from html.parser import HTMLParser
from lxml.html import tostring

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
max_id = comments['max_id']
max_type = comments['max_id_type']
comments_data = comments['data']
rows = []

print('正在爬第1页')
for comment in comments_data:
    time = comment['created_at']
    text = comment['text']
    user_id = comment['user']['id']
    user_name = comment['user'][0]['screen_name']
    user_gender = comment['user']['gender']
    user_des = comment['user']['description']
   
    row = [user_id, user_name, user_gender, user_des, text, time]
    rows.append(row)

i=1
# page = int(input('爬几页:'))
page = 2
for i in range(1, page):
    i += 1
    print('正在爬第%i页'%i)
    url = base_url.format(max_id=max_id, max_type=max_type, weiboid=weiboid)
    response = req.get(url, headers=headers, timeout=10)
    data = response.json()

    # Filter information that we want
    comments = data.get('data')
    max_id = comments['max_id']
    max_type = comments['max_id_type']
    comments_data = comments['data']
    rows = []

    for comment in comments_data:
        time = comment['created_at']
        text = comment['text']
        user_id = comment['user']['id']
        user_name = comment['user'][0]['screen_name']
        user_gender = comment['user']['gender']
        user_des = comment['user']['description']
   
        row = [user_id, user_name, user_gender, user_des, text, time]
        rows.append(row)

## 设置excel表地址
dest_filename = '/Users/siyuyang/Desktop/TNT-1/data.xlsx'
## 将数据写入Excel
from openpyxl import Workbook
wb = Workbook()
# 选中活动表
ws1 = wb.active
 
# 设置表头
title = ['用户id', '用户名', '性别', '用户描述', '评论', '评论时间']
for row in range(len(title)):
    c = row + 1
    ws1.cell(row=1, column=c, value=title[row])
 
# 数据录入
for listIndex in range(len(rows)):
    ws1.append(rows[listIndex])
 
wb.save(filename=dest_filename)
