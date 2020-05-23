'''
def st_rank():
	N=int(input())
	s=''
	for n in range(N):
		s+=' '+str(input())
	s=s.strip()
	while '  ' in s:
		s=s.replace('  ',' ')


	A=[float(i) for i in s.split(' ')]
	for i in range(1,N):
		for j in range(0, N-i):
			if A[j*2+1] > A[(j+1)*2+1] or ( A[j*2+1] == A[(j+1)*2+1] and A[j*2] < A[(j+1)*2] ):
				A[j*2], A[j*2+1], A[(j+1)*2],A[(j+1)*2+1] = A[(j+1)*2],A[(j+1)*2+1], A[j*2],A[j*2+1]




	for j in range(N):
		print(format(A[2*j],'.2f'), format(A[2*j+1],'.3f'))

	






st_rank()
'''


def st_rank(s):
	A=[float(i) for i in s.split(' ')]
	N=int(A[0])
	A=A[1:]
	print(A)
	for i in range(1,N):
		for j in range(0, N-i):
			if A[j*2+1] > A[(j+1)*2+1] or ( A[j*2+1] == A[(j+1)*2+1] and A[j*2] < A[(j+1)*2] ):
				A[j*2], A[j*2+1], A[(j+1)*2],A[(j+1)*2+1] = A[(j+1)*2],A[(j+1)*2+1], A[j*2],A[j*2+1]
				print(A)


	for j in range(N):
		print(format(A[2*j],'.2f'), format(A[2*j+1],'.3f'))

	






#st_rank('3 1.8 70 1.75 70 1.8 69.5')
st_rank('5 1.8 70 1.75 70 1.8 69.5 1.5 65.333 1.91 65.333')



