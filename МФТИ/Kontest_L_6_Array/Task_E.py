def st_sort():
	
	S=[]
	I=''
	
	while I!='#':
		I=str(input())
		
		S.append(I)
	
	#S=['10','0 3','0 10','2 3','6 4','6 1','9 9','2 2','2 4','1 5','#']
	#S=['3','2 4','0 10','2 1','2 1','1 2','1 2','0 3','#']
	
	N=int(S[0])
	S=S[1:-1]

	for i in range(len(S)):
		S[i]=[int(j) for j in S[i].split(' ')]




	R=[0]*N
	for k in range(len(S)):
		R[S[k][0]]+=S[k][1]


	for bypass in range(1, len(S)):   # сортирвка по первому символу
		for k in range(0, len(S)-bypass):
			if S[k][0]<S[k+1][0]: 
				S[k], S[k+1] = S[k+1], S[k]
			if S[k][1]<S[k+1][1] and S[k][0]==S[k+1][0]:
				S[k], S[k+1] = S[k+1], S[k]






	for bypass in range(1, len(S)):   # сортирвка по первому символу
		for k in range(0, len(S)-bypass):
			if R[S[k][0]]<R[S[k+1][0]]: 
				S[k], S[k+1] = S[k+1], S[k]
			if S[k][1]<S[k+1][1] and S[k][0]==S[k+1][0]:
				S[k], S[k+1] = S[k+1], S[k]


	result=[]

	for m in S:
		result.append(m[1])





	return ' '.join([str(i) for i in result])







print(st_sort())









	
'''


	S=['3','0 3','0 10','2 3','2 2','2 4','1 5','#']




'''
