# /c/Users/brill/Desktop/Crawring/venv/Scripts/python
# -*- Encoding : UTF-8 -*-

from bs4 import BeautifulSoup

print("library imported")

def main():
    #객체 초기화, 뒤에있는 parser가 핵심: python에서 접근 가능하게 만들어줌
    soup = BeautifulSoup(open("data/index.html"), "html.parser")
    print(soup)

if __name__ == "__main__":
    main()
    