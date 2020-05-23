h=input(int())
a=h%10
if a<h:
    b=(h-a)/10%10
else:
    b=0
if (h-a)/10>b:
    c=((h-a)/10-b)/10%10
else:
    c=0
    
d=a+b+c

print(int(d))
