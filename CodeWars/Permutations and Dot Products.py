def function(A, B):
	A.sort()
	B.sort(reverse=True)
	min_dot=0
	for i in range(len(A)):
		min_dot+=(A[i]*B[i])

	return(min_dot)




























def my_test(function):
	print('Test ')
	print('testcase #1: ', end='')
	test_list_1, test_list_2=[1,2,3,4,5], [0,1,1,1,0]
	control_case=6
	test_try=function(test_list_1, test_list_2)
	print ('Ok' if test_try==control_case else 'Fail')

	print('testcase #2: ', end='')
	test_list_1, test_list_2=[1,2,3,4,5], [0,0,1,1,-4]
	control_case=-17
	test_try=function(test_list_1, test_list_2)
	print ('Ok' if test_try==control_case else 'Fail')


	print('testcase #3: ', end='')
	test_list_1, test_list_2=[1,3,5], [4,-2,1]
	control_case=-3
	test_try=function(test_list_1, test_list_2)
	print ('Ok' if test_try==control_case else 'Fail')





if __name__ == '__main__':
	my_test(function)