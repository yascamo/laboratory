import math
print("ax^2+bx+c")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b**2-4*a*c
print ("discriminant = ")
if d > 0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2 =(-b-math.sqrt(d))/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)
if d == 0:
    x = -b/(2*a)
    print("x = ", x)
if d < 0:
    print("net korney")