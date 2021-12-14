# /c/ProgramData/Anaconda3/python
# -*- conding: utf-8 -*-

'''
# 모방은 또 하나의 창조이다.
# pd.DataFrame Source
# https://github.com/pandas-dev/pandas/blob/v1.2.4/pandas/core/frame.py#L394-L9477
# 간단한 상속 예제
'''

import pandas as pd
temp_dict = {"A": [1,2,3],
             "B": [4,5,6]}

temp = pd.DataFrame(temp_dict, columns=["B", "A"])
print(temp)


class newDataFrame(pd.DataFrame):
    pass

temp2 = newDataFrame(temp_dict,
                     columns=["A", "B", "C"])
print("---")
print(temp2)