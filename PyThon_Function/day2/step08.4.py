# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# check_closure

def check_closure(arg1, arg2):
    def inside_func():
        print("arg1 was {}".format(arg1))
        print("arg2 was {}".format(arg2))

    return inside_func()

if __name__ == "__main__":
    my_func = check_closure(10, 200)
    #값이 잘 들어가 있는지 확인
    print(my_func.__closure__ is not None)

    #2개의 변수가 존재 하는지 확인
    print(len(my_func.__closure__) == 2)

    #closure value 확인
    closure_values = [
        my_func.__closure__[i].cell_contents for i in range(2)
    ]

    print(closure_values == [10, 200])


# 변수가 제대로 들어 갔는지 확인 해 주는 함수
# filtering, closure에 값이 자 들어갔는지 확인


