#/c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# context manager : @Context... 에대한 이야기, 잠깐 쓰고 없어지는 것들
# Processing = context setting, cord run, context delete


def main():
    # context manager * 중요 !
    with open("../data/myFile.txt") as file:
        text = file.read()
        text_length = len(text)

    print("file 글자의 총 길이는 {} 이다.".format(text_length))

if __name__ == "__main__":
    main()
