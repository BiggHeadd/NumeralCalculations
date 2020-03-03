# coding: utf-8
"""
commit "Chart 1 code"
"""
import math

# config
x0 = 2
h0 = 0.32
EPS = 0.4e-4

H = []
DTF = []
DQF = []
ERR = []

def DELTF(x, h):
    return math.log((x+h)/x)

def FormProblem():
    """
    get the x0 and h0 from user
    return x0, h0
    """
    x0 = float(input("Enter x0: "))
    h0 = float(input("Enter h0: "))
    return x0, h0

def Operation(x0, h0):
    """
    operate the nearest value of ln(x0)'
    """
    H.append(h0)
    DTF.append(DELTF(x0, h0))
    DQF.append(DTF[0] / h0)
    ERR.append(1)
    while ERR[-1] > EPS:
        H.append(H[-1] / 2)
        DTF.append(DELTF(x0, H[-1]))
        DQF.append(DTF[-1] / H[-1])
        ERR.append(abs(DQF[-1] - DQF[-2]))

def ShowTable():
    print("="*70)
    print("{:^3}\t{:^10}\t{:^12}\t{:^12}\t{:^12}\t".format("K", "H[K]", "DTF[K]", "DQF[K]", "ERR[K]"))
    print("-"*70)
    for k in range(len(H)):
        print("{:2}\t{:10.6f}\t{:12.8e}\t{:12.8e}\t{:12.8e}\n".format(k, H[k], DTF[k], DQF[k], ERR[k]))
    print("-"*70)
    print("ANS = {}".format(DQF[-1]))
    print("="*70)

def SaveTable(x0, h0):
    with open("./TB_x0_{}_h0_{}.txt".format(x0, h0), 'w', encoding='utf-8')as f:
        f.write("="*62 + "\n")
        f.write("{:^3}\t{:^10}\t{:^12}\t{:^12}\t{:^12}\t\n".format("K", "H[K]", "DTF[K]", "DQF[K]", "ERR[K]"))
        f.write("-"*62 + "\n")
        for k in range(len(H)):
            f.write("{:2}\t{:10.6f}\t{:12.8e}\t{:12.8e}\t{:12.8e}\n".format(k, H[k], DTF[k], DQF[k], ERR[k]))
        f.write("-"*62 + "\n")
        f.write("ANS = {}".format(DQF[-1]) + "\n")
        f.write("="*62 + "\n")
    print("Save done!")


def main():
    x0, h0 = FormProblem()
    Operation(x0, h0)
    ShowTable()
    SaveTable(x0, h0)

if __name__ == "__main__":
    main()