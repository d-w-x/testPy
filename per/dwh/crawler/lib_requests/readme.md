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
3. `response.url`，资源url；`response.status_code`，状态码；
   `response.encoding`，编码`ISO-8859-1`。

## 其他设置

1. 请求头设置：`header={}, response = requests.request(url=url,
   method="GET", headers=header)`。
2. GET方式参数设置：`params={}, response = requests.request(url=url,
   method="GET", params=params)`。使用`params`;or request.get()
3. POST方式设置参数：`data={}, response = requests.request(url=url,
   method="POST", data=data)`。使用`data`;or request.post()
4. 代理:`proxy = {}， response = requests.request(url=url, method="GET",
   proxies=proxy)`。

## 获取需要多次请求的页面

```python
import requests
url4 = "http://****/login.php"
data = {}
session = requests.Session()
session.post(url=url4, data=data)    #先登录获取登录信息
response = session.get("http://***/otherPage")    #请求其他页面
response.close()
```

注意：使用同一个`session`。

## 不信任的SSL证书

提示： `requests.exceptions.SSLError:
HTTPSConnectionPool(host='vpn.nju.edu.cn', port=443): Max retries
exceeded with url: / (Caused by SSLError(SSLCertVerificationError(1,
'[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed
certificate (_ssl.c:1056)')))`

```python
import requests
url = "https://vpn.nju.edu.cn/"
response = requests.request(url=url, method="GET", verify=False)
response.close()
```

---

注意：

1. 除了 HEAD, Requests 会自动处理所有重定向。`allow_redirects =
   False`禁止重定向；可以使用响应对象的 history 方法来追踪重定向。
2. `timeout`设置相应时间。
3. 异常：

   >1. 遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个
   >   ConnectionError 异常。
   >2. 如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status()
   >   会抛出一个 HTTPError 异常。
   >3. 若请求超时，则抛出一个 Timeout 异常。
   >4. 若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
   >5. 所有Requests显式抛出的异常都继承自
   >   requests.exceptions.RequestException 。

4. 文件一般以二进制形式存取。
