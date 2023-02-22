a = 4
b = 2
c = 1
if a > b and a < c:
    z = a**2 + b*c
elif a > c:
    z = (a+b)**2
else:
    z = (b+c)**2
print(z)