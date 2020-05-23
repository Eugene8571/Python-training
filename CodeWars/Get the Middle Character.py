def get_middle(A):
	c=len(A)//2
	if len(A)==1:
		return A
	elif len(A)%2==1:
		return A[c]
	return str(A[c-1]+A[c])


def my_test(function):
	print('Testing', function.__doc__)
	print('testcase #1: ', end='')
	test_input='asdffff'
	control_case='f'
	function_output=function(test_input)
	print ( 'Ok' if function_output==control_case else 'Fail', function_output) 	


	print('testcase #3: ', end='')
	test_input='testing'
	control_case='t'
	function_output=function(test_input)
	print ('Ok' if function_output==control_case else 'Fail', function_output) 


	print('testcase #2: ', end='')
	test_input='a'
	control_case='a'
	function_output=function(test_input)
	print ('Ok' if function_output==control_case else 'Fail', function_output) 	

	print('testcase #3: ', end='')
	test_input='asda'
	control_case='sd'
	function_output=function(test_input)
	print ('Ok' if function_output==control_case else 'Fail', function_output) 



if __name__ == '__main__':
	my_test(get_middle) 