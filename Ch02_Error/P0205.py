# coding: utf-8
import math
PI = math.pi
X = [3.14, 3.142, 3.1416, 3.14159,
     3.14159265, 3.141592653, PI]

Y, REX, REY = [], [], []


def Operation():
    for x in X:
        y = math.tan(x / 4)
        REX.append(abs(PI - x) / PI)
        REY.append(abs(1.0 - y) / y)
        Y.append(y)


def ShowTable():
    print("="*70)
    print("{:^3}\t{:^10}\t{:^12}\t{:^12}\t{:^12}".format(
        "k", "X[k]", "Y[k]", "REX[k]", "REY[k]"))
    print("-"*70)
    k = 0
    for x, y, rex, rey in zip(X, Y, REX, REY):
        print("{:2}\t{:10.10f}\t{:12.8e}\t{:12.8e}\t{:12.8e}\n".format(
            k, x, y, rex, rey))
        k += 1
    print("="*70)


def SaveTable(filename):
    with open(filename, 'w', encoding='utf-8')as f:
        f.write("="*70 + "\n")
        f.write("{:^3}\t{:^10}\t{:^12}\t{:^12}\t{:^12}\n".format(
            "k", "X[k]", "Y[k]", "REX[k]", "REY[k]"))
        f.write("-"*70)
        k = 0
        for x, y, rex, rey in zip(X, Y, REX, REY):
            f.write("{:2}\t{:10.10f}\t{:12.8e}\t{:12.8e}\t{:12.8e}\n".format(
                k, x, y, rex, rey))
            k += 1
        f.write("="*70 + "\n")


if __name__ == "__main__":
    Operation()
    ShowTable()
    SaveTable("TB062.TXT")
