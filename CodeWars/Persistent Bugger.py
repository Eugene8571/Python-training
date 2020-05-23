def persistence(num):
	S=str(num)
	n=0
	while len(S)>1:
		loc_mult=1
		for s in S:
			loc_mult*=int(s)
		S=str(loc_mult)
		n+=1
	return(n)



print(persistence(999))