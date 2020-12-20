def often():
	
	N=int(input())
	A=[]
	for i in range(N):
		A.append(int(input()))
	'''
	N=4
	A=[5,5,2,5]
	'''
	
	C=0
	res=-1
	for x in range(N):
		loc_C=0
		for y in range(x, N):
			if A[x]==A[y]:
				loc_C+=1
		if loc_C>C:
			C=loc_C
			res=A[x]
	return res

print(often())