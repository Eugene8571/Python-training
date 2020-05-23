def find_it(A):
	count=0

	for i in range(len(A)):
		if count%2==1:
			return(count)
		
		for num in A:

			if A[i]==num:
				count+=1

























assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5, 'Fail'
print('Test is OK')