# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# def cnt_letter(content, letter):
#     """content 안에 있는 문자를 세는 함수 Docstring
#     #google style
#     Args:
#         content(str) : 탐색 문자열
#         letter(str) : 찾을 문자열
#
#     Return:
#         int
#     #code 작업
#     """
#     return None

# if __name__ == "main":
#     a=1
#     b=3
#     print(add(a,b))
#     print(cnt_letter())

def cnt_letters(content, letter):
    """content 안에 있는 문자를 세는 함수 Docstring
    #google style
    Args:
        content(str) : 탐색 문자열
        letter(str) : 찾을 문자열

    Return:
        int
        """
    #code 작업
    print("함수Test")
    return (len([char for char in content if char == letter]))
    # 리스트 컴프리헨션
    return non

if __name__=="__main__":
     docstring = cnt_letters.__doc__
     border = "*" *20
     print('{}\n{}\n{}'.format(border, docstring, border))
