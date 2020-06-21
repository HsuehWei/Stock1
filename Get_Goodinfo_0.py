'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Python_讀取股票歷年經營績效_以遠東新1402為例_01_使用pandas與BeautifulSoup取得網頁資料
# http://dboffat.blogspot.com/2018/12/import-requestsfrom-bs4-import.html
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=1402'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
r = requests.get(url, headers = headers)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
rows = soup.find('div', {"id": "divFinDetail"}).find('table', {"class": "solid_1_padding_4_0_tbl"})
dfs = pd.read_html(str(rows))
print (dfs[0])
dfs[0].to_html("1402.html",index=False)