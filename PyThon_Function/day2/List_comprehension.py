# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# pythonic way

# 문자열 쪼개기, List에 저장

letters = []
temp_string = "green"


if __name__ == "__main__":
    for text in temp_string: # green
        letters.append(text)
    print(letters)

print("*************************************")

if __name__ == "__main__":
    letters2 =[text for text in temp_string]
    print(letters2)

