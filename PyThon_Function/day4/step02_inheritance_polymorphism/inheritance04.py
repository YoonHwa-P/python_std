# /c/ProgramData/Anaconda3/python
# -*- conding: utf-8 -*-

'''
- 클래스 메서드 사용
- 날짜 입력 예제
'''

from datetime import datetime

class BetterDate:
    # Constructor

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_str(cls, datestr):

        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        return cls(year, month, day)

    @staticmethod
    def from_str2(datestr):
        parts = datestr.split("-")
        BetterDate.year, BetterDate.month, BetterDate.day = int(parts[0]), int(parts[1]), int(parts[2])
        return BetterDate.year, BetterDate.month, BetterDate.day

    @classmethod
    def from_datetime(cls, dateobj):
        year, month, day = dateobj.year, dateobj.month, dateobj.day
        return cls(year, month, day)

if __name__ == "__main__":
    bd_str = BetterDate.from_str("2021-04-26")
    print("---- Date String ----")
    print(bd_str.year)
    print(bd_str.month)
    print(bd_str.day)

    bd_str2 = BetterDate.from_str2("2021-04-26")
    print("---- Date String2 ----")
    print(bd_str2[0])
    print(bd_str2[1])
    print(bd_str2[2])

    today = datetime.today()
    bd_str = BetterDate.from_datetime(today)
    print("---- Date Dateime ----")
    print(bd_str.year)
    print(bd_str.month)
    print(bd_str.day)