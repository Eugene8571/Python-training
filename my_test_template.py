def function(a):
	pass



def my_test(function):
	print('Тест ', function.__doc__)
	print('testcase #1: ', end='')
	test_case=''
	control_case=''
	test_try=function(test_case)
	print ('Ok' if test_try==control_case else 'Fail') 	            

if __name__ == '__main__':
	my_test(function)