# 发送请求的模块
import requests
# 解析html代码的工具
from lxml import etree

import os
# UA伪装
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
# 指定url地址
hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list_resp = requests.get(hero_list_url,headers=headers)
# print(hero_list_resp.json())
for h in hero_list_resp.json():
    ename = h.get('ename')
    cname = h.get('cname')

    if  not os.path.exists(cname):
        os.makedirs(cname)

    # 访问英雄主页
    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{ename}.shtml'
    hero_info_resp = requests.get(hero_info_url,headers=headers)
    hero_info_resp.encoding = 'gbk'
    e = etree.HTML(hero_info_resp.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    names = [name[0:name.index('&')] for name in names.split('|')]

    # 发送请求
    for i,n in enumerate(names):
        resp = requests.get(f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg',headers=headers)

        # 接收服务器响应的图片
        # 保存图片
        # 将图片保存到相应的问价夹中
        with open(os.path.join(cname, f'{n}.jpg'), 'wb') as f:
            f.write(resp.content)
        print(f'已下载：{n}的皮肤')