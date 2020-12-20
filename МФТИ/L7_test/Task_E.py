def tribo(n):
	A=[0,0,1]
	for i in range(3,n+1):
		A.append(A[i-3]+A[i-2]+A[i-1])
	return A[n]

def superior_tribo():
	a=int(input())

	for b in range(10000):
		if tribo(b)>a:
			return b

print(superior_tribo())