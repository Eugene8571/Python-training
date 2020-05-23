def dirReduc(A):
	s=' '.join(A)
	
	while True:
		b=s
		s=s.replace('NORTH SOUTH','')
		s=s.replace('SOUTH NORTH','')
		s=s.replace('WEST EAST','')
		s=s.replace('EAST WEST','')

		while '  ' in s:
			s=s.replace('  ',' ')

		if b == s:
			break
	
	s=s.strip()

	B=s.split(' ')
	return B


'''
def dirReduc(A):
	if len(A)<=1:
		return A
	
	for i in range(1, len(A)):
		W_E=0
		N_S=0
		if A[i] == 'WEST':
			W_E+=1
		if A[i] == 'EAST':
			W_E-=1
		if A[i] == 'NORTH':
			N_S+=1
		if A[i] == 'SOUTH':
			N_S-=1

		if A[i-1] == 'WEST':
			W_E+=1
		if A[i-1] == 'EAST':
			W_E-=1
		if A[i-1] == 'NORTH':
			N_S+=1
		if A[i-1] == 'SOUTH':
			N_S-=1

		if W_E == 0 and N_S == 0:
			A=A[:i-1]+A[i+1:]
			return dirReduc(A)


	return A
'''

		




from my_test import test
test(dirReduc, ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"], ['WEST'])
test(dirReduc, ["NORTH", "WEST", "SOUTH", "EAST"], ["NORTH", "WEST", "SOUTH", "EAST"])

