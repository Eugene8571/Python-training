def solution(n):
	'''Roman Numerals Encoder'''
	Roman_dictionary={0:'', 1:'I', 5:'V',10:'X', 50:'L', 100:'C', 500:'D', 1000:'M' }
	dict_keys=list(Roman_dictionary.keys())
	for i in range(len(dict_keys)//2):
		dict_keys[i], dict_keys[len(dict_keys)-i-1]=dict_keys[len(dict_keys)-i-1], dict_keys[i]
	print(dict_keys)
	Roman_Style=''
	for i in dict_keys:
		if n//i in dict_keys: 
			Roman_Style+=Roman_dictionary[n//i]
		else:
			Roman_Style+=Roman_dictionary[n//i//(i+1)]
	return (Roman_Style)



















def my_test(function):
	print('Testing ', function.__doc__ if function.__doc__!=None else '-------------')
	
	print('Test #1: ', end='')
	test_input=6
	expecting_output='VI'
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output, ' shold be ', expecting_output)

	print('Test #2: ', end='')
	test_input=9
	expecting_output='XI'
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output, ' shold be ', expecting_output)

	print('Test #3: ', end='')
	test_input=1666
	expecting_output='MDCLXVI'
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output, ' shold be ', expecting_output)

my_test(solution)