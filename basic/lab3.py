import urllib.request
import re

url = "http://finance.naver.com/item/main.nhn?code=005930"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))

stock_results = re.findall("(\<dl class=\blind\"\>)([\s\S]+?)(\<\dl\>)"), html_contents)
sam_stock = stock_results[0]
sam_index = sam_stock[1]

index_list = re.findall("(\dd\>)([\s\S]+?)(\<\/dd\>)"), sam_index)

for index in index_list:
    print(index[1])
