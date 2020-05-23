def d_sum(number):
	res=0
	s=str(number)
	for k in range(len(s)):
		res+=int(s[k])
		
	return res




def order_weight(s):
	if s=='':
		return ''
	A=[int(i) for i in s.split(' ')]
	N=len(A)
	for pos in range(0, N-1):
		for k in range(pos+1, N):
			if d_sum(A[k])<d_sum(A[pos])\
			or (d_sum(A[k])==d_sum(A[pos]) and str(A[k])<str(A[pos])):
				A[k], A[pos] = A[pos], A[k]

	

	return ' '.join(str(i) for i in A)




from my_test import test

test(order_weight, "103 123 4444 99 2000", "2000 103 123 4444 99")
test(order_weight, "2000 10003 1234000 44444444 9999 11 11 22 123", "11 11 2000 10003 22 123 1234000 44444444 9999")
test(order_weight, "", "")
