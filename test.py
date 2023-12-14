import math

a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))

delta = b**2 - 4*a*c
s = math.sqrt(delta)
if delta < 0:
    print("Phuong trinh vo nghiem")
    if delta == 0:
        x1 = x2 = -b / (2*a)
        print("Phuong trinh co nghiem kep la ", x1)
else:
    x1 = (-b + s) / (2*a)
    x2 = (-b - s) / (2*a)
    print("Phuong trinh co 2 nghiem phan biet: ")
    print("Nghiem 1 la: ", x1)
    print("Nghiem 2 la: ", x2)