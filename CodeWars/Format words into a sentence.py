def format_words(a):
	'''Format words into sentence'''
	S=''
	if a==None or len(a)==0 or a==['']:
		return('')
	B=[]
	#print(type(a))
	if type(a) is str:
		#print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		A=[str(i)for i in a.split(', ')]
		a=A
	#print(len(a))

	if type(a) is list:
		for word in a:
			if len(word)>0:
				B.append(word)
	a=B
			

	if len(a)==1:
		return(str(a[0]))


	for word in a:
		#print(a[len(a)-1])

		S+=word
		if a.index(word)!=len(a)-2 and a.index(word)!=len(a)-1:
			S+=', '
		elif a.index(word)==len(a)-2:
			S+=' and '
		else:
			return(S)












def my_test(function):
	print('Testing', function.__doc__)

	print('Test #1: ', end='')
	test_input=['archer', 'ninja', 'samurai', 'ronin']
	expecting_output="ninja, samurai and ronin"
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output)


	print('Test #2: ', end='')
	test_input=['ninja', '', 'ronin']
	expecting_output="ninja and ronin"
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output)

	print('Test #3: ', end='')
	test_input=[]
	expecting_output=""
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output)


	print('Test #4: ', end='')
	test_input=['', '', 'three']
	expecting_output='three'
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output)



	print('Test #5: ', end='')
	test_input=None
	expecting_output=''
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output)

	print('Test #5: ', end='')
	test_input='abc, abcdefghijklmnopqrstuvw, abcdefghijklmnopqrstuvwx, abcdefghijklmn, abcdefghijklmnopqrs, abcdefghijk, abcdefghijklmnopqrs, abcd'
	expecting_output='abc, abcdefghijklmnopqrstuvw, abcdefghijklmnopqrstuvwx, abcdefghijklmn, abcdefghijklmnopqrs, abcdefghijk, abcdefghijklmnopqrs and abcd'
	actual_output=function(test_input)
	print('OK' if expecting_output==actual_output else 'Fail')
	print(actual_output)





my_test(format_words)