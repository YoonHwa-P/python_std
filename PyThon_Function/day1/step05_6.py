#/c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

import contextlib
import time

@contextlib.contextmanager
def timer():
    """ 시간 측정하는 context manager 관리 함수

    yield:
        None

    """

    start = time.time()
    yield
    end = time.time()

    print("시간측정(Elapsed): {: .2f} sec".format(end-start))

def main():
    with timer():
        print("How long spend time ?")
        time.sleep(0.25) #크롤링 할 때 종종 사용

if __name__ == "__main__":
    main()


    #시간 측정을 미리 해 보고 data 전체를 돌리면 어떻게 될지 예측 해 볼 수 있다.


