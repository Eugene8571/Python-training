def reverse_word():
	N=int(input())
	A=[]
	for i in range(N):
		s=str(input())
		A.append(s[::-1]+' '+s)


	for i in range(1,N):
		for j in range(0,N-i):
			if len(A[j]) > len(A[j+1])\
			 or (len(A[j]) == len(A[j+1]) and A[j][0:int(len(A[j])//2)] > A[j+1][0:int(len(A[j+1])//2)]):
				A[j],A[j+1] = A[j+1],A[j]

	
	L=0
	for i in range(N):
		if len(A[i])>L:
			L=len(A[i])
			print(int((L-1)/2))
		print(A[i])

reverse_word()

