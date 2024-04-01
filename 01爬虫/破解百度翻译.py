import requests

# 指定url
post_url = 'https://fanyi.baidu.com/sug'
# 进行UA伪装
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# post请求参数处理（同get请求一致）

while True:
	print('（退出翻译请输入1）')
	word1 = input('请输入你想翻译的单词：')
	if word1 == '1' :
		break
	data = {
		'kw':word1
	}
	# 请求发送
	response = requests.get(url=post_url,headers=headers,data=data)
	# 获取响应数据：json()方法返回的是obj（如果确认响应数据是json类型的，才可以使用json()）
	dic_obj = response.json()

	print(dic_obj)
	
print("此次翻译结束，翻译内容源自百度翻译")