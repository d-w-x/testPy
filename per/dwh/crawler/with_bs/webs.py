from bs4 import BeautifulSoup as bs

soup = bs(open("tencent.html", "r+", encoding="UTF-8"), "lxml")
# print(soup.prettify())
evens = soup("tr", class_="even")
# for even in evens:
#    print(even)
trs = soup.find_all("tr", class_={"even", "odd"})[1:]
# print(trs[0].prettify())
print(trs[0].name)
print(trs[0].attrs)
print(trs[0].contents)
for tr in trs:
    # print(a)
    # print("=" * 30)
    tds = tr.find_all(lambda x: x.has_attr('class'))
    print(list(tds))
    # aTag = tds[0].find("a")
    # href = "https://hr.tencent.com/" + aTag['href']
    # print(href)
    # print(aTag.string)
    # print(tds[3].string)
    # s = list(tr.stripped_strings)
    # print(s)
