<center>python爬虫学习</center>

要进行 Python 爬虫，需要具备以下知识：

1. Python 编程语言：了解 Python 的基本语法、数据类型、控制流程等基础知识，能够编写和理解 Python 的代码。
2. 网络基础知识：了解 HTTP 协议、URL 结构、HTML 基础等网络知识，理解网页的组成和请求响应过程。
3. 爬虫框架和库：熟悉 Python 中常用的爬虫框架和库，如 Requests、BeautifulSoup、Scrapy 等，掌握如何使用它们来发送请求、解析网页、提取数据等。
4. 数据解析和处理：了解常见的数据解析和处理技术，如正则表达式、XPath、CSS 选择器等，能够根据网页的结构和需求提取所需的数据。
5. 数据存储：了解数据存储的方法和工具，如将数据保存到文件、数据库或者其他数据存储介质中。
6. 反爬虫策略：了解常见的反爬虫策略，如验证码、限制访问频率、动态加载等，能够应对一些简单的反爬虫手段。
7. 代码调试和异常处理：具备良好的调试能力，能够排查和解决代码中的错误和异常情况。

爬虫的核心：

* 爬取网页：爬取整个网页，包含了网页中所有的内容
* 解析数据：将网页中得到的数据进行解析
* 难点：爬虫与反爬虫之间的博弈

## 学习过程中项目

### 1.NBA球员信息爬取

### 2.破解百度翻译

### 3.王者荣耀皮肤爬取

* 此次爬虫均主要使用requests请求
* 学习了基本的UA伪装，并未接触更深层的反爬手段
* 学习到了如何使用xpath将网页中需要的数据一层层取出
* 体会到从很多数据中找到自己想要的的难度

### 4.人脸识别

在图片显示的环节就遇到问题，经搜索研究发现是由于图片路径问题，处理方法：将cv.imread('')中的路径写全并将\ (单斜杠)改为 \ \ (双斜杠)

#### 1.环境配置

* 需要下载opencv模块

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple      opencv包在cmd中输入即可

* 需要在opencv官网下载源码来使用分类器

#### 2.调整人脸检测准确度

1. 调整 scaleFactor 参数：scaleFactor 决定了每个图像尺度的缩放比例，较小的值会导致更精确的检测，但速度较慢。
2. 调整 minNeighbors 参数：minNeighbors 指定在目标周围需要检测到的邻居数量。较大的值会过滤掉一些错误检测。
3. 调整 minSize 和 maxSize 参数：minSize 和 maxSize 分别指定检测到的人脸的最小和最大尺寸。
4. 使用其他人脸检测器

#### 3.opencv中数据训练的原理

分为两方面：特征提取和分类器训练

* 特征提取

​		人脸识别的第一步是将图像中的人脸区域提取出来，并将其转换为可用于分类的特征向量。OpenCV 中常用的特征提取算法是 Haar 特征和 LBP（Local Binary Patterns）特征（本次使用的是LBP特征）。

​		Haar 特征是一种基于矩形的特征描述符，它可以用来检测图像中的各种形状，包括人脸。LBP 特征则是一种用于纹理分析的局部二值模式，它可以有效地描述人脸的纹理信息。

* 分类器训练

​		在特征提取之后，需要使用分类器对提取到的特征向量进行训练。OpenCV 中常用的分类器是基于机器学习算法的级联分类器（Cascade Classifier）。

​		训练分类器的过程中，需要提供正样本（包含人脸的图像）和负样本（不包含人脸的图像）（此次学习中并未学习到），通过迭代优化分类器的权重，使其能够准确地区分人脸和非人脸。

#### 4.基于LBPH的人脸识别

​	LBPH将检测到的人脸分为小单元，并将其与模型中的对应单元进行比较，对每个区域的匹配值产生一个直方图。（由于这种方法的灵活性，LBPH是唯一允许模型样本人脸和检测到的人脸在形状、大小上可以不同的人脸识别算法）

​	调整后的区域中调用predict()函数，该函数返回两个元素的数组

* 第一个元素是所识别个体的标签
* 第二个是置信度评分

置信度：

所有的算法都有一个置信度评分阈值，置信度评分用来衡量所识别人脸与原模型的差距

* 0表示完全匹配
* 一个好的识别参考值要低于100
* 高于80的参考值会被认为是低的置信度评分

## 一、requests

### 1.基本使用

#### 1.安装

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

### 2.response的属性以及类型

* r.text

获取网站源码

* r.encoding

访问或定制编码方式

* r.url

获取请求的url

* r.content

响应的字节类型

* status_code

响应的状态码

* headers

响应的头信息

### 3.requests_get请求

get请求时最常见的http请求方法，用于请求服务器发送指定的资源

```python
# url 请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url,params,kwargs)
```

eg：

```python
import requests
url = 'https://www.baidu.com/s?'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
data = {
	'wd':'北京'
}
response = requests.get(url=url,parmas=data,headers=headers)
content = response.text
print(content)
```

总结：

* 参数使用params传递
* 参数无需urlencode编码
* 不需要请求对象的定制
* 请求资源路径中的？可加可不加

### 4.requests_post请求

post请求用于将数据提交到指定的资源处理

```python
response = requests.post(url,data=data)
```

eg：

```python
import requests
post_url = 'http://fanyi.baidu.com/sug'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
data = {
	'kw':'eye'
}
r=requests.post(url=url,headers=hearders,data=data)
```

总结：

* post请求 是不需要编解码
* post请求的参数是data
* 不需要请求对象的定制

### 5.requests代理

当ip被封后可以改代理

eg：

```python
import requests
url = 'https://www.baidu.com/s?'

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
data = {
	'wd'='ip'
}

proxy = {
    'http':'.....'
}
response = requests.get(url,params=data,headers=headers,proxies = proxy)
content = response.text
with open('daili.html','w',encoding'utf-8')as fp:
	fp.write(content)
```

### 6.requests_cookie登录

跳过验证码登录

## 

