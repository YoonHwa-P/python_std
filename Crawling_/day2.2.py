# /c/Users/brill/Desktop/Crawring/venv/Scripts/python
# -*- Encoding : UTF-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def main():

    custom_header = {
        "referer" : "https://www.naver.com/",
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    url = "https://www.naver.com/"
    req = requests.get(url, headers = custom_header)
    soup = BeautifulSoup(req.text, "html.parser")
    # print("know status : " , req.status_code)
    # print(soup.prettify())
    titles = []
    hrefs = []
    div = soup.find("div", class_ = "list_issue")
    for a in div.find_all("a"):
        # print("url : ", a)
        # print("title ", a.get_text())
        # print("HREF URL : ", a["href"])
        titles.append(a.get_text)
        hrefs.append(a["href"])

    df = pd.DataFrame({"news": titles, "url": hrefs})
    df["datetime"] = datetime.now()
    df = df[["datetime", "news", "url"]]
    df.to_excel("data/naver_Head_new.xlsx", index=False)


    # 나머지는 노가다 : 태그 찾고, 구조 확인하고, 전처리 하고고

if __name__ == "__main__":
    main()