# 自带爬虫库`urllib`

## 简单的直接请求

```python
from urllib import request
url = "http://www.baidu.com/"
response = request.urlopen(url)
```

## 修改头文件的请求

```python
from urllib import request
url = "http://www.baidu.com/"
header = {}
req = request.Request(url, headers=header)
response = request.urlopen(req)
```

## 使用代理

```python
from urllib import request
import random
url = "http://httpbin.org/ip"
proxy_list = [{"http" : "61.135.217.7:80"},
              {"http" : "111.155.116.245:8123"},
              {"http" : "122.114.31.177:808"},]
proxy = random.choice(proxy_list)
proxy_handler = request.ProxyHandler(proxy)
requests = request.Request(url)
opener = request.build_opener(proxy_handler)
response = opener.open(requests)
response.close()
```

注意：

1. `request.build_opener(proxy_handler)`使用该语句则修改request的默认代理。
2. 代理的第一个参数表示支持的协议，一般为`http`或者`https`。
3. `proxy_handler=urllib.request.ProxyHandler({"http" :"username:password@ip:port"})`使用私密代理
4. 免费没好货，分秒就过期

## 保存cookies:

```python
from urllib import request
from http.client import HTTPResponse
from http import cookiejar
cookie = cookiejar.MozillaCookieJar('cookies.txt')
cookie_processor = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(cookie_processor)
requests = request.Request("http://www.baidu.com")
response: HTTPResponse = opener.open(requests)
cookie.save()
response.close()
```

注意：

1. 如果需要保存（写入文件），则使用`MozillaCookieJar`或者`LWPCookieJar`实现，他们是两种不同的存储协议。
2. 如果仅存在内存中，则用超类`FileCookieJar`即可。
3. `ignore_discard=True`保存会过期的cookie，`ignore_expires=True`保存已经过期的cookie
4. `cookie.load()`加载指定的cookie文件

## post请求

```python
from urllib import request,parse
url = "http://httpbin.org/post"
forms = {"i": "internet",
         "action": "FY_BY_CLICKBUTTION",
         "Chinese": "的复杂性",
         "typoResult": "false"
         }
data = parse.urlencode(forms).encode("UTF-8")
requests = request.Request(url, data=data, method="POST")
response = request.urlopen(requests)
response.close()
```

注意：url编码+[encode()](../../Built_in_Types/iterable_types/strings/readme.md#string的其他方法)为字符串