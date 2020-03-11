# coding: utf-8
import math

PI = math.pi

x = 0.25 * PI
delt_x = 0.25 * PI

# optional
delt_x *= 1.0e-8

x = 0.5 * PI - delt_x

y1 = math.sin(delt_x)
y2 = math.cos(x)
y3 = math.cos(delt_x)
y4 = math.sin(x)

print("y1 = {}".format(y1))
print("y2 = {}".format(y2))
print("y3 = {}".format(y3))
print("y4 = {}".format(y4))