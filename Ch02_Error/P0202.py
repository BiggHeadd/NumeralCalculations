# coding: utf-8
import math

PI = math.pi

def f(x):
    return math.tan(x)

def df(x):
    return 1.0 / math.cos(x) / math.cos(x)

if __name__ == "__main__":
    x0 = 3.14 / 6.0
    x1 = PI / 6.0

    y0 = math.tan(x0)
    y1 = math.tan(x1)

    REX = (x1 - x0) / x0
    REY = (y1 - y0) / y0

    CND = x0 * df(x0) / f(x0)
    CRE = CND * REX

    print("REX = {:.15e}".format(REX))
    print("REY = {:.15e}".format(REY))
    print("CND = {:.15e}".format(CND))
    print("CRE = {:.15e}".format(CRE))