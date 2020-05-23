def F(n):
	Fib=[0,1]
	for i in range(2,n+1):
			Fib.append(Fib[i-2]+Fib[i-1])

	return Fib[n]



def productFib(prod):
	for i in range(1000):
		if F(i)*F(i+1)==prod:
			return [F(i), F(i+1), True]
		if F(i)*F(i+1) < prod and prod < F(i+1)*F(i+2):
			return [F(i+1), F(i+2), False]



print(productFib(5895))