def sum_of_multiples(N):
	S=0
	for n in range(N):
		if n%3==0 or n%5==0:
			S+=n
	return S





















A=sum_of_multiples(10)
print(A)