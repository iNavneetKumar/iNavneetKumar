x = int(input("Enter a value ="))
a = ('Area of a square=', x*x)
b = ('Perimeter of a square=', 4*x)
c = ('Radius=', x/2)
d = ('Diameter=', x*2)
e = ('Area of Circle=', 22/7*x**2)
f = ('Circumference of Circle=', 2*22/7*x)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


for x in range(10,20):
    if(x % 2==0):
        print(x)
