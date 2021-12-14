# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# 시간 측정 decorator function
import time


def timer(func):
    """ 함수 실행 시간 확인
    :param func: check할 함수 넣을거임
    :return: 걸린 시간
    """
    def wrapper(*args, **kwargs):
        #현재 시간
        time_start = time.time()

        #decorated fuction 불러오기
        result = func(*args, **kwargs)
        time_total = time.time() - time_start
#"시간측정(Elapsed): {: .2f} sec".format(end-start)
        print("{}, Total time is {: .2f} sec.".format(func.__name__, time_total))

        return result
    return wrapper

@timer
def check_time(num):
    time.sleep(num)

if __name__ == "__main__":
    check_time(1.5)


secs = time.time()
print(secs)

tm = time.gmtime(secs)
print(tm)

tm = time.localtime(secs)
print("year:", tm.tm_year)
print("month:", tm.tm_mon)
print("day5:", tm.tm_mday)
print("hour:", tm.tm_hour)
print("minute:", tm.tm_min)
print("second:", tm.tm_sec)

string = time.ctime(secs)
print(string)



tmt = time.localtime(secs)
string = time.strftime('%Y-%m-%d %I:%M:%S %p', tmt)
print(string)


string = '2021-12-07 07:00:54 PM'
tmm = time.strptime(string, '%Y-%m-%d %I:%M:%S %p')
print(tmm)


print("Start-->")
time.sleep(1.5)
print("<--End")