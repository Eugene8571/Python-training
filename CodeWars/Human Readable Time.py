def make_readable(c):
	SS=c%60
	MM=(c-SS)//60%60
	HH=(c-SS-MM*60)//60//60%100

	T=['00']*3
	if len(str(SS))==1:
		T[2]='0'+str(SS)
	else:
		T[2]=str(SS)

	if len(str(MM))==1:
		T[1]='0'+str(MM)
	else:
		T[1]=str(MM)

	if len(str(HH))==1:
		T[0]='0'+str(HH)
	else:
		T[0]=str(HH)



	return ':'.join(T)
	#return str(HH) + ':'+ str(MM) + ':' + str(SS)



print(make_readable(11181))
