

def deta_manipulations():
	a=''
	A=[]
	while str(a)!='#':
		a=str(input())
		if a!='#':
			A.append(int(a))


	sum_x=0
	for x in A:
		sum_x+=x
		A_median=round((sum_x/len(A)), 3)
	
	A_max=max(A)

	A_min=min(A)


	A_tripl=0
	i=-1
	if len(A)>=3:
		while i<=len(A):
			print(i)
			i+=3
			#print (A[i-2], A[i-1], A[i], '%', A[i], A_tripl)
			A_tripl += (A[i-2]+A[i-1]+A[i])%A[i]
			#print(A_tripl)
	answer = str(A_median)+' '+str(A_max)+' '+str(A_min)+' '+str(A_tripl)
	return(answer)


print(deta_manipulations())




