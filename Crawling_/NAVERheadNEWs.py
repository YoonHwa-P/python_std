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

    print("know status : " , req.status_code)

if __name__ == "__main__":
    main()