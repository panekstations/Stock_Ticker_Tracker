import requests
import lxml.html
from lxml import etree

ISIN = 'FR0013393188'

# Original Link
'https://markets.ft.com/data/funds/tearsheet/historical?s=FR0010929794'


# enter date into list [yyyy, mm, dd]
start = [2020, 1, 31] 
end = [2020, 2, 2]


url = f'https://markets.ft.com/data/equities/ajax/get-historical-prices?startDate={start[0]}%2F{start[1]}%2F{start[2]}&endDate={end[0]}%2F{end[1]}%2F{end[2]}&symbol=535683133'


html = requests.get(url)
doc = lxml.html.fromstring(html.content)
# print(url)

result= doc.text
print(result)
