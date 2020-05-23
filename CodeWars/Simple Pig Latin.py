def pig_it(S):
	A=[str(i) for i in S.split(' ')]
	for i in range(len(A)):
		
		simbol=''

		if A[i].isalpha()==False:
			simbol=A[i][len(A[i])-1]
			A[i] = A[i][:-1]

		
		if len(A[i])>=2:
			A[i] = A[i] + A[i][0] + 'ay' + simbol
			A[i] = A[i][1:]

		if len(A[i])==1:
			A[i] = A[i] + 'ay' + simbol

		if len(A[i])==0:
			A[i] = simbol


		
	return ' '.join(A)

print(pig_it('Pig latin is cool, ye ?'))