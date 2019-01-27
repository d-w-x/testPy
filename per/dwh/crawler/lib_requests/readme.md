# 第三方爬虫库`requests`

## 简单的直接请求

```python
import requests
url = "http://www.baidu.com"
response = requests.request(url=url,method="GET")
print(response.text)
```

注意：
1. text自行解码,是Unicode数据，高概率产生乱码
2. content是字节流，`response.content.decode()`自行解码即可。
3. `response.url`，资源url；`response.status_code`，状态码； `response.encoding`，编码`ISO-8859-1`。

## 其他设置
1. 请求头设置：`header={}, response = requests.request(url=url, method="GET", headers=header)`。
2. GET方式参数设置：`params={}, response = requests.request(url=url, method="GET", params=params)`。使用`params`。
3. POST方式设置参数：`data={}, response = requests.request(url=url, method="POST", data=data)`。使用`data`。
4. 代理:`proxy = {}， response = requests.request(url=url, method="GET", proxies=proxy)`。
5. 


