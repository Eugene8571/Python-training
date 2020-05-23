def accum(A):
	S=''
	n=1
	for x in A:
		X=x*n
		X=X.capitalise()
		S+=X
		S+='-'
		n+=1
	S=S.rstrip('-')
	return(S)
