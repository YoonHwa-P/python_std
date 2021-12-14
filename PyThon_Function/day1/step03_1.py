# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-
# 함수의 규칙
## 한 함수에는 하나씩의 Function만 있어야 한다.
# 1. 가독성이 떨어지기 때문에.
# 2. 확장성이 떨어지기 때문.
# ---Eventually 하나의 함수에는 하나의 Function만 있게 한다.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def load_and_plot(datasetname):
    """data를 불러오고 그래프를 작성 한다.
        Args :

    return:

    """
    # 작업 1 : data를 불러오는 코드 작성 : DB 연결하는 code 작성
    data = sns.load_dataset(datasetname)

    y = data.iloc[:, 1].values
    x = data.columns
    num_list = data.select_dtypes(include = [np.number]).columns
    print("column name : ", num_list)

    # 작업 2 : 시각화 코드 작성
    sns.scatterplot(x= num_list[0], y=num_list[1], data = data)
    plt.show()

    # 작업 3 : Return
    return x, y

if __name__ == "__main__":
    x,y = load_and_plot("tips")
    print("x is : ", x)
    print("y is : ", y)

