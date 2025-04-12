a = ["Juan", 20, 1.8, True]
print(a[len(a)-1])
print(a[-1])
print(a[-2])

b = [4,2,6,3]
print(len(b))
print(sum(b))
print(max(b))
print(min(b))

c = a + b
print(c)

for x in b:
 print(x)

a = "mesa"
b = "silla"
print(a,b)
tmp = a 
a = b
b = tmp
print(a,b)
a,b = b,a
print(a,b)
def suma5(e,f):
 return e+5, f+5
print(suma5(2,5))
x,y =suma5(2,5)
print(x, y)
