# /c/Users/brill/Desktop/Crawring/venv/Scripts/python
# -*- Encoding : UTF-8 -*-

from bs4 import BeautifulSoup

print("........library imported")

def main():
    # 객체 초기화
    soup = BeautifulSoup(open("data/index2.html"), "html.parser")
    # 원하는 data 출력
    print(soup.find("div", class_ = "elice").find("p").get_text())
    # 저장(Excel:pandas, DB)

if __name__ == "__main__":
    main()
