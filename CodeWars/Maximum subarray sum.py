def maxSequence(A):

	max_sum=max([sum(A), 0])
	sub_a=A
	sub_a.append(0)
	for i in range(len(A)):
		
		sub_a=sub_a[:-1]
		print(sub_a)
		if sum(sub_a)>max_sum: 
			max_sum=sum(sub_a)
		sub_b=sub_a
		for j in range(len(sub_a)):
			sub_b=sub_b[1:]
			if sum(sub_b)>max_sum:
				max_sum=sum(sub_b)

	return max_sum

		
















#[-2, 1, -3, 4, -1, 2, 1, -5, 4]

#print(maxSequence([-2, 1, -3, 4, -1, 2, 1]))

#print(maxSequence([4, -1, 2, 1, -5, 4]))

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

