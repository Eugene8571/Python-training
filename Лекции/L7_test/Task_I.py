
'''
def max_stable():
	A=[]
	while 0 not in A:
		A.append(int(input()))
	A=A[:-6]
	return max(A)

print(max_stable())
'''


def max_stable():
	A=[]
	sub_max=-10000
	while 0 not in A:
		A.append(int(input()))
		if len(A)==7:
			if A[0]>sub_max:
				sub_max=A[0]
			A=A[1:]
	return sub_max

print(max_stable())