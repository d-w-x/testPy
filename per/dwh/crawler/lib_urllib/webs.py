from http import cookiejar
from http.client import HTTPResponse
from urllib import request, parse

# ================init=====
url = "http://httpbin.org/ip"
response: HTTPResponse = request.urlopen(url)
with open("a.json", "w+", encoding='utf-8') as file:
    file.write(response.read().decode("UTF-8"))
response.close()

# ================header====
header = {"accept": "*/*",
          "Connection": "keep - alive",
          "X-Requested-With": "XMLHttpRequest",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
          }
req = request.Request(url, headers=header)
response = request.urlopen(req)
with open("a.json", "a", encoding='utf-8') as file:
    file.write(response.read().decode("UTF-8"))
response.close()

# ================Proxy====
proxy = {}
proxy_handler = request.ProxyHandler({})
requests = request.Request(url, headers=header)
opener = request.build_opener(proxy_handler)
response: HTTPResponse = opener.open(requests)
with open("a.json", "a", encoding='utf-8') as file:
    file.write(response.read().decode("UTF-8"))
response.close()

# ================Save cookie====
cookie = cookiejar.MozillaCookieJar('cookies.txt')
cookie_processor = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(cookie_processor)
requests = request.Request("http://www.baidu.com", headers=header)
response: HTTPResponse = opener.open(requests)
cookie.save(ignore_discard=True, ignore_expires=True)
response.close()

# ================post====
url = "http://httpbin.org/post"
forms = {"i": "internet",
         "action": "FY_BY_CLICKBUTTION",
         "Chinese": "的复杂性",
         "typoResult": "false"
         }
data = parse.urlencode(forms).encode("UTF-8")
requests = request.Request(url, data=data, headers=header, method="POST")
response = request.urlopen(requests)
with open("a.json", "a", encoding='UTF-8') as file:
    file.write(response.read().decode("UTF-8"))
response.close()
