# coding: utf-8
import math

PI = math.pi
x0 = 3.1416 / 6
x1 = PI / 6

if __name__ == "__main__":
    u0 = math.sin(x0)
    u1 = math.sin(x1)

    y0 = math.exp(u0)
    y1 = math.exp(u1)

    # 计算绝对误差
    REX = abs((x1 - x0) / x0)
    REU = abs((u1 - u0) / u0)
    REY = abs((y1 - y0) / y0)

    # 计算条件数
    CNUX = x0 * math.cos(x0) / u0
    CNYU = u0
    CNYX = CNYU * CNUX
    
    # 通过条件数*绝对误差得到相对误差
    CREYU = CNYU * REU
    CREYX = CNYX * REX

    print("REX   = {:.15e}".format(REX))
    print("REU   = {:.15e}".format(REU))
    print("REY   = {:.15e}".format(REY))
    print("CNUX  = {:.15e}".format(CNUX))
    print("CNYU  = {:.15e}".format(CNYU))
    print("CNYX  = {:.15e}".format(CNYX))
    print("CREYU = {:.15e}".format(CREYU))
    print("CREYX = {:.15e}".format(CREYX))