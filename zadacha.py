print("ax^2+bx+c")
a = input("a = ")
b = input("b = ")
c = input("c = ")
d = b**2-4*a*c
print ("Discriminant = ")
if d > 0:
    x1=(-b+sqrt(d))/(2*a)
    x2 =(-b-sqrt(d))/(2*a)
    print("x1 = ")