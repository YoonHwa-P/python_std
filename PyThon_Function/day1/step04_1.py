# /c/Users/brill/Desktop/PyThon_Function/venv/Scripts/python
# -*- coding : utf-8 -*-


# --- About : def iloc(a = None) ---
# mutable : 변경이 가능한, list, dicr, set, bytearray, objects, functions
# immutable : 변경이 어려운, tuple, int, float, bool, string, bytes


def list_a(var=[]): #mutable
    var.append(1)
    return var

def list_b(var = None): #immutable _ 이렇게 짜라
    if var is None:
        var = []
    var.append(1)
    return var

if __name__ == "__main__":
    print(list_a())
    print(list_a())
    print(list_a())
    print("-----------")
    print(list_b())
    print(list_b())
    print(list_b())