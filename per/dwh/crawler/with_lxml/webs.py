from lxml import etree

parser = etree.HTMLParser(encoding="UTF-8")
html = etree.parse("tencent.html", parser=parser)

# 输出链接
# trs = html.xpath("//td[@class='l square']/a/@href")
# for tr in trs:
#     print("https://hr.tencent.com/"+tr)


trs = html.xpath("//tr[@class='odd']|//tr[@class='even']")
for tr in trs:
    name = tr.xpath(".//a/text()")
    print(name[0])
    tds = tr.xpath(".//td/text()")
    for td in tds:
        print(td)
    print()
