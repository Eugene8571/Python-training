def tribonacci(signature, n):
	if n==0:
		return []
	
	res=[0]*n
	for i in range(n):
		if i<3:
			res[i]=signature[i]
		else:
			res[i]=res[i-3]+res[i-2]+res[i-1]
	return res





print(tribonacci([1,1,1],10))