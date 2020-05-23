def test(function, test_input, expecting_output):
	#print('Testing ', function.__doc__ if function.__doc__!=None else '-------------')
	print('Test #:', end=' ')
	if isinstance(test_input,list):
		if len(test_input)==1 or test_input is not list:
			actual_output=function(test_input[0])
		if len(test_input)==2:
			actual_output=function(test_input[0], test_input[1])
		if len(test_input)==3:
			actual_output=function(test_input[0], test_input[1], test_input[2])
	else:
		actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail  '+\
		'actual_output: ' + str(actual_output) + '  expecting_output: ' + str(expecting_output))
	