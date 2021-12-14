# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

import pandas
import pandas as pd

def add_new_column(new_vals, data= pd.DataFrame()):
    """ 새로운 column을 data에 추가, column name is  columns_<n> 형태로 저장. 이때 모두 numeric으로 저장
    :param new_vals: (iterable) 함수 실행 때마다 새로운 컬럼의 값 의미
    :param data:  (dataframe, optional) : 함수가 실행되면 업데이트됨
        만약 df로 입렭받지 못하면, 임의의 df이 디폴트로 생성됨.
    :return:
        DataFrame
    """
    data['col_{}'.format(len(data.columns))] = new_vals
    return data

if __name__ == "__main__":
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))



# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

import pandas
import pandas as pd


def add_new_column(new_vals, data=None):
    """ 새로운 column을 data에 추가, column name is  columns_<n> 형태로 저장. 이때 모두 numeric으로 저장
    :param new_vals: (iterable) 함수 실행 때마다 새로운 컬럼의 값 의미
    :param data:  (dataframe, optional) : 함수가 실행되면 업데이트됨
        만약 df로 입렭받지 못하면, 임의의 df이 디폴트로 생성됨.
    :return:
        DataFrame
    """
    if data is None :
        data = pd.DataFrame()
    data['col_{}'.format(len(data.columns))] = new_vals
    return data


if __name__ == "__main__":
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))
    print(add_new_column(new_vals=range(10)))
    print(add_new_column(new_vals=None))








