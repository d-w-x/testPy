import requests

# ================init=====
# url = "http://www.baidu.com"
url = "http://httpbin.org/get"
response = requests.request(url=url, method="GET")
with open("a.html", "w+", encoding='utf-8') as file:
    file.write(response.content.decode("UTF-8"))
response.close()

# ================header====
header = {"accept": "*/*",
          "Connection": "keep - alive",
          "X-Requested-With": "XMLHttpRequest",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
          }
response = requests.request(url=url, method="GET", headers=header)
with open("a.html", "a", encoding='utf-8') as file:
    file.write(response.content.decode("UTF-8"))
response.close()

# ================get=====
params = {"un": "123321", "kw": "123456"}
response = requests.request(url=url, method="GET", headers=header, params=params)
with open("a.html", "a", encoding='utf-8') as file:
    file.write(response.content.decode("UTF-8"))
response.close()

# ================post=====
urls = "http://httpbin.org/post"
data = {"un": "123321", "kw": "123456"}
response = requests.request(url=urls, method="POST", headers=header, data=data)
with open("a.html", "a", encoding='utf-8') as file:
    file.write(response.content.decode("UTF-8"))
response.close()

# ================proxy=====
proxy = {"http": "101.132.122.230:3128"}
response = requests.request(url=url, method="GET", headers=header, proxies=proxy)
with open("a.html", "a", encoding='utf-8') as file:
    file.write(response.content.decode("UTF-8"))
response.close()
