


R=[]

a=7

for n in range(a):
	if n == 0 or n == 1:
		R.append(1)
	else:
		c=R[n-1]+R[(n-2)]
		R.append(c)
print(R)

