# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-

# bulit in 변수 > 전역변수 (gloval) > nonLocal > 지역변수 (Local)


print("Case 01--------")
x=100
def a():
    x=40
    return print(x)

if __name__ == "__main__":
    print(a())
    print(x)

print("------------------------")
print(" ")


print("Case 02--------")

x=100
def a():
    global x # <-- 글로벌로 선언되어 글로벌 x가 100에서 40으로 재 선언됨
    x=40
    return print(x)

if __name__ == "__main__":
    print(a())
    print(x)

print("------------------------")

print(" ")
print("Case 03--------")
# Non Local
def b():
    y= 10

    def c():
        y=100
        print(y)
    b() # <-- 100
    print(y) # <-- 10

if __name__ == "__main__":
    print(b())
    print(y)

print("------------------------")

print(" ")
print("Case 04--------")


# Non Local
def d():
    y = 10

    def e():
        nonlocal y
        y = 100
        print(x)

    d()  # <-- 100
    print(y)  # <-- 100


if __name__ == "__main__":
    print(d())
    print(y)