def move_zeros(A):
	B=[]
	z=[]
	for s in A:
		if s is not bool() and s==0:
			z.append(s)
		else:
			B.append(s)
	B.extend(z)
	return B


print(move_zeros(['a', 'b', None, False, 'd', 1, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

