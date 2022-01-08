# /c/Users/brill/Desktop/Crawring/venv/Scripts/python
# -*- Encoding : UTF-8 -*-

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from datetime import datetime
import time
import pandas as pd

def main():
    company_code = "005930" # 삼성전자
    url = "https://finance.naver.com/item/sise_day.nhn?code=" + company_code
    ua = UserAgent()
    headers = {"User-agent": ua.ie}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)

    last_page = int(soup.select_one("td.pgRR").a["href"].split('=')[-1])
    # print(last_page)

    df = None
    count = 0
    for page in range(1, last_page + 1):
        req = requests.get(f'{url}&page={page}', headers=headers)
        # print(pd.read_html(req.text, encoding="euc-kr"))
        df = pd.concat([df, pd.read_html(req.text, encoding="euc-kr")[0]], ignore_index=True)
        if count > 10:
            break
        count += 1
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    print(df.head())
    print(df.tail())

if __name__ == "__main__":
    main()