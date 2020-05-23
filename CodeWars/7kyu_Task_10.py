def Descending_Order(num):
	if num < 10:
		return(num)
	N=[int(i) for i in str(num)]
	L=len(N)





	
	for i in range(L-1):
		for x in range(L-1):
			if N[x]<N[x+1]:
				N[x], N[x+1] = N[x+1], N[x]

	
	S=''
	for i in N:
		S+=str(i)


	return(int(S))






	

Res=Descending_Order(12349977545656789)
print(Res)