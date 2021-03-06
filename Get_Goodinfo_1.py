'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Python_讀取股票歷年經營績效_以遠東新1402為例_01_使用pandas與BeautifulSoup取得網頁資料
# http://dboffat.blogspot.com/2018/12/import-requestsfrom-bs4-import.html
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import requests
from bs4 import BeautifulSoup
import pandas as pd 

#基本現況
def Info_hitory(stock) :
    url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=' + str(stock)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    r = requests.get(url, headers = headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find('div', {"id": "divFinDetail"}).find('table', {"class": "solid_1_padding_4_0_tbl"})
    dfs = pd.read_html(str(rows))
    print (dfs[0])
    dfs[0].to_html("1402.html",index=False)

#本益比
def PE_history(stock) :
    url = 'https://goodinfo.tw/StockInfo/ShowK_ChartFlow.asp?RPT_CAT=PER&STOCK_ID=' + str(stock) + '&CHT_CAT=WEEK'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    r = requests.get(url, headers = headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find('div', {"id": "divDetail"}).find('table', {"class": "solid_1_padding_4_0_tbl"})
    dfs = pd.read_html(str(rows))
    print (dfs[0])
    dfs[0].to_html("1402.html",index=False)

#每月營收
def Revenue_byMonth_history(stock) :
    url = 'https://goodinfo.tw/StockInfo/ShowSaleMonChart.asp?STOCK_ID=' + str(stock)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    r = requests.get(url, headers = headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find('div', {"id": "divDetail"}).find('table', {"class": "solid_1_padding_4_2_tbl"})
    dfs = pd.read_html(str(rows))
    print (dfs[0])
    dfs[0].to_html("1402.html",index=False)

#經營績效
def Performance_history(stock) :
    url = 'https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=' + str(stock)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    r = requests.get(url, headers = headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find('div', {"id": "divFinDetail"}).find('table', {"class": "solid_1_padding_4_0_tbl"})
    dfs = pd.read_html(str(rows))
    print (dfs[0])
    dfs[0].to_html("1402.html",index=False)
    
#現金流量
def CashFlow_history(stock) :
    url = 'https://goodinfo.tw/StockInfo/StockCashFlow.asp?STOCK_ID=' + str(stock)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    r = requests.get(url, headers = headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find('div', {"id": "divDetail"}).find('table', {"class": "solid_1_padding_4_1_tbl"})
    dfs = pd.read_html(str(rows))
    print (dfs[0])
    dfs[0].to_html("1402.html",index=False)

#PE_history(3529)
#Info_hitory(3529)
#Revenue_byMonth_history(3529)
#Performance_history(3529)
CashFlow_history(3529)

