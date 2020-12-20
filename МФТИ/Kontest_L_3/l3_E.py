# no 'if' no '**'
def bin_log(N):
	n=1
	s=2
	while s<N:
		s=s*2
		n+=1
	return(n)


A=bin_log(int(input()))

print(A)




#print(bin_log(4))
#print(bin_log(10))
#print(bin_log(1627))