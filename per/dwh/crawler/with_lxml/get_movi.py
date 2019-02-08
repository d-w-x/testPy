import requests
from lxml import etree

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml",
    "Accept-Encoding": "gzip",
    "Accept-Language": "zh-CN,zh",
    "Host": "movie.douban.com",
    "Referer": "https://movie.douban.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
resp = requests.get("https://movie.douban.com/cinema/nowplaying/nanjing/", headers=headers)
html = etree.HTML(resp.text)
lists = html.xpath("//div[@id='nowplaying']/div[2]/ul[@class='lists'][1]/li")
movies = []
for li in lists:
    name = li.xpath(".//@data-title")[0]
    score = li.xpath(".//@data-score")[0]
    time = li.xpath(".//@data-duration")[0]
    region = li.xpath(".//@data-region")[0]
    director = li.xpath(".//@data-director")[0]
    actors = li.xpath(".//@data-actors")[0]
    pic = li.xpath("./ul/li/a/img/@src")[0]
    movie = {
        "name": name,
        "score": score,
        "time": time,
        "region": region,
        "direcitor": director,
        "actors": actors,
        'pic': pic}
    movies.append(movie)
print(movies)
