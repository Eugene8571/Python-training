def solve(A):


	if A==sorted(A):
		return 'A' # Ascending
	

	if A==sorted(A, reverse=True):
		return 'D' # Descending


	N=len(A)
	if N==3:
		if A[1]>A[2]:
			return 'RD'
		return 'RA'



	left=[A[0],A[1],A[2]]
	right=[A[N-3],A[N-2],A[N-1]]




	if left==sorted(left) or right==sorted(right):
		return 'RA'
	return 'RD'

	












print (solve([1,2,3,4,5,7]))
print(solve([9,8,7,6,5,4,3,2,1,0]))
print (solve([12,1,2,3,4,5,6,7]))
print(solve([9,8,7,6,5,4,3,2,1,0,15,14]))
print(solve([9,6,7]))
print(solve([5,9,3]))