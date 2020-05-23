def in_circle_check(s):
	A=[int(n) for n in s.split(' ')]
	ans=''
	if (A[0]**2+A[1]**2) <= A[2]**2 :
		ans='YES'
		#return('YES')
	else:
		ans='NO'
		#return('NO')
	return ans


T=in_circle_check(str(input()))
print(T)
















def function(a):
	pass



def my_test(function):
	print('Тест ', function.__doc__)
	print('testcase #1: ', end='')
	test_case='-1 3 1'
	control_case='NO'
	test_try=function(test_case)
	print ('Ok' if test_try==control_case else 'Fail') 	            

if __name__ == '__main__':
	my_test(in_circle_check)