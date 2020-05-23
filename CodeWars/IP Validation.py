def is_valid_IP(strng):

    A=[int(i) for i in strng.split('.') \
    if i.isdecimal() \
    if 0<=int(i)<=255 \
    if len(i)==len(str(int(i)))]
    
    if len(A)==4 and len([int(i) for i in strng.split('.')])==4:
    	return True
    return False





def my_test(function):
	print('Testing', function.__doc__)
	print('testcase #1: ', end='')
	test_input='abc.def.ghi.jkl'
	control_output=False
	function_output=function(test_input)
	print ( 'Ok' if function_output==control_output else 'Fail', function_output) 	

	print('testcase #2: ', end='')
	test_input='123.456.789.0'
	control_output=False
	function_output=function(test_input)
	print ( 'Ok' if function_output==control_output else 'Fail', function_output) 

	print('testcase #3: ', end='')
	test_input='12.255.56.1'
	control_output=True
	function_output=function(test_input)
	print ( 'Ok' if function_output==control_output else 'Fail', function_output) 

	print('testcase #4: ', end='')
	test_input='12.600.255.56.1'
	control_output=False
	function_output=function(test_input)
	print ( 'Ok' if function_output==control_output else 'Fail', function_output) 

	print('testcase #5: ', end='')
	test_input='123.045.067.089'
	control_output=False
	function_output=function(test_input)
	print ( 'Ok' if function_output==control_output else 'Fail', function_output) 

if __name__ == '__main__':
	my_test(is_valid_IP) 