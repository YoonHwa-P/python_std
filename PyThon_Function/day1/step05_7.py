#/c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

#

import contextlib
import step05_6 # time 재는 함수 있는 file, utils에 넣어 놓으면 좋다.
import time


@contextlib.contextmanager
def openReadOnly(fileName):
    """

    :param fileName:
    :return:
    """

    read_file = open(fileName, mode="r", encoding="UTF-8")
    yield read_file

    read_file.close()

def main(fileName):
    with openReadOnly(fileName) as file:
        text = file.read() # 파일 전체를 읽어오기

    n=0
    for word in text.split():
        if word in ["오미크론", "코로나"]:
            n +=1
    print("오미크론 및 코로나 단어의 개수는 {} 이다.".format(n))


if __name__ == "__main__":
    fileName = "../data/newsArticle.txt"
    with step05_6.timer():
        main(fileName)
        time.sleep(0.25)



