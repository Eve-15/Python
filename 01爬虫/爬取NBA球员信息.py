

# pip install requests
import requests
# pip install etree
from lxml import etree

# 发送地址
url = 'https://nba.hupu.com/stats/players'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# 发送请求
resp = requests.get(url,headers = headers)
# 处理结果
e = etree.HTML(resp.text)
# 解析相应的数据
numb = e.xpath('//table [@class="players_table"]//tr/td[1]/text()')
names = e.xpath('//table [@class="players_table"]//tr/td[2]/a/text()')
teams = e.xpath('//table [@class="players_table"]//tr/td[3]/a/text()')
scores = e.xpath('//table [@class="players_table"]//tr/td[4]/text()')



# 是否保存
with open("nba.text","w",encoding='utf-8') as f:

    for num,name,team,score in zip(numb,names,teams,scores):
        f.write(f'排名：{num} 姓名：{name} 球队：{team} 得分{score}\n')