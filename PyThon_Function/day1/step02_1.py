# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-
# 정규화: normalization ~ Standatdzation (표준화 : z-score)
# data의 범위를 0과 1로 변환해서 data의 분포를 조정하는 방법
#  data 분석 정규화 공식 --> 확인 2장
# y = (x - min(x))/ (Max(x)-min(x)) : 최대 최소 정규화
# Min_Max normalization
# pandas data frame

import seaborn as sns

def min_max_normalize(column):
    """data를 정규화 하는 함수
    Args :
        column (pandas Series) : 정규화를 하기 위한 것

    return: Series
        pandas series: min_max 정규화 공식의 답을 가져온다.
    :param column:
    :return:
    """

    min_max_score = (column-column.min())/ (column.max() - column.min())
    return min_max_score

if __name__ == "__main__":
    iris = sns.load_dataset("iris")
    print(iris.head())

    iris['sepal_length'] = min_max_normalize(iris['sepal_length'])
    iris['sepal_width'] = min_max_normalize(iris['sepal_width'])
    iris['petal_length'] = min_max_normalize(iris['petal_length'])
    iris['petal_width'] = min_max_normalize(iris['petal_width'])
    print(iris.head())


# machine learning 전의 feature Engineering