# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

"""
모방 : 부모 클래스를 모방 후 자식이 창조
"""

import pandas as pd

class newDataFrame(pd.dataFrame):
    pass

temp_dic = {"A": [1, 2, 3],
            "B":[4, 5, 6]}

if __name__ == "__main__":
    temp = pd.DataFrame(temp_dic, columns=["A","B"])
    print(temp)
    print("-----------------")
    temp2 = newDataFrame(temp_dic, columns=["B", "A"])
    print(temp2)