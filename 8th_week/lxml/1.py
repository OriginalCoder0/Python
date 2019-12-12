from lxml import etree

f = open("./test.html", "r", encoding="utf-8")
content = f.read()
f.close()

# 解析html文档，并返回根节点对象
html = etree.HTML(content)
result = html.xpath("/html/head/title/text()")

print(result)


result = html.xpath("//li/a/text()")
print(result)
