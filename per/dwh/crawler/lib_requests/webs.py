import requests

# ================init=====
url = "http://httpbin.org/get"
url3 = "http://www.baidu.com"
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
url2 = "http://httpbin.org/post"
data = {"un": "123321", "kw": "123456"}
response = requests.post(url=url2, headers=header, data=data)
# response = requests.request(url=urls, method="POST", headers=header, data=data)
with open("a.html", "a", encoding='utf-8') as file:
    file.write(response.content.decode("UTF-8"))
response.close()

# ================proxy=====
proxy = {"HTTP": "118.24.156.214:8118"}
response = requests.request(url=url, method="GET", headers=header, proxies=proxy)
with open("a.html", "a", encoding='utf-8') as file:
    file.write(response.content.decode("UTF-8"))
response.close()

# ================多次请求=====
# url4 = "http://*/login/index.php"
# data = {
#     "username": "username",
#     "password": "password"
# }
# session = requests.Session()
# # session.post(url=url4, headers=header, data=data)
# response = session.get("http://*/view.php?id=143")
# with open("b.html", "w+", encoding='utf-8') as file:
#     file.write(response.content.decode())
# response.close()

# ================ssl证书=====
url5 = "https://vpn.nju.edu.cn/"
response = requests.request(url=url5, method="GET", headers=header, verify=False)
with open("a.html", "a", encoding='utf-8') as file:
    file.write(response.content.decode("UTF-8"))
response.close()

# ================pictures====
url6 = "https://timgsa.baidu.com/timg?image&quality=80&" \
       "size=b9999_10000&sec=1548683266478&di=fe33720f42451b0f9d58e27cf946d415&imgtype=0&" \
       "src=http%3A%2F%2Fatt.bbs.duowan.com%2Fforum%2F201207%2F10%2F1643377kz171k67km611x4.jpg"
response = requests.request(url=url6, method="GET", headers=header, verify=False)
with open("s.jpeg", "wb+") as file:
    file.write(response.content)
