# /c/Users/brill/Desktop/Crawring/venv/Scripts/python
# -*- Encoding : UTF-8 -*-

import requests
print("requests library is loaded")


def main():
    url = "https://blog.naver.com/abcdpuh"
    req = requests.get(url)
    #상태 코드 확인
    print("status : ", req.status_code)
    # Test Extrection
    print(req.text)
    print("loop")

def try_except_main():
    try:
        url = "https://www.naver.com/11111"
        req = requests.get(url)
        req.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    finally:
        print("loop")


if __name__ == "__main__":
    main()
    try_except_main()