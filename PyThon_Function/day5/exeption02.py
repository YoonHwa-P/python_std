# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : UTF-8

def try_func(x, idx):
    try:
        return 100/x[idx]
    except ZeroDivisionError:
        print("did't divide zero")
    except IndexError:
        print("not in range of Index")
    except TypeError:
        print("there is type Error")
    except NameError:
        print("it is not definated parameter")
    finally:
        print("무조건 실행됨")


def main():
    a = [50, 60, 0, 70]
    print(try_func(a,1))

    # Zero Division Error
    print(try_func(a,0))

    # Index Error
    print(try_func(a,5))

    # type Error
    print(try_func(a, "hi"))


if __name__ == "__main__":
    main()
