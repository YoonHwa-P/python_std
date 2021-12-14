# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-
# 수치형 data 표준화, 종모양 정규 분포를 따르는 data 를 만들어 주기 위해 해 주는 표준화
# 표준화 (공식) 찾아서 함수 작성 해서 iris data에 적용
# x' = (x - mean) / std
import seaborn as sns

def standardization(column):
    """data를 표준화 하는 함수
    Args :
        column (pandas Series) : 표준화를 하기 위한 것

    return: Series
        pandas series: 정규분포를 갖는 data series를 가져온다.
    :param column:
    :return:
    """
    mean_var_score = (column - column.mean()) / column.std()
    return mean_var_score


if __name__ == "__main__":
    irisV = sns.load_dataset("iris")
    print(irisV.head())

    irisV['sepal_length'] = standardization(irisV['sepal_length'])
    irisV['sepal_width'] = standardization(irisV['sepal_width'])
    irisV['petal_length'] = standardization(irisV['petal_length'])
    irisV['petal_width'] = standardization(irisV['petal_width'])
    print(irisV.head())


# --- same upon ---
def zScore(column):
    """data를 정규화 하는 함수
    Args :
        column (pandas Series) : 표준화를 하기 위한 것

    return: Series
        pandas series: 정규분포를 갖는 data series를 가져온다.
    :param column:
    :return:
    """
    zScore_ = (column - column.mean()) / column.std()
    return zScore_


if __name__ == "__main__":
    irisvs = sns.load_dataset("iris")
    print(irisvs.head())

    irisvs['sepal_length'] = zScore(irisvs['sepal_length'])
    irisvs['sepal_width'] = zScore(irisvs['sepal_width'])
    irisvs['petal_length'] = zScore(irisvs['petal_length'])
    irisvs['petal_width'] = zScore(irisvs['petal_width'])
    print(irisvs.head())