




h=int(input())
a=h
a=h%10
#print(a)
b=int((h-a)/10)
b=b%10
#print(b)
c=int((((h-a)/10)-b)/10)
#print(c)
r=a+b+c
print(r)
