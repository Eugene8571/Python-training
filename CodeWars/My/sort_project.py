def insert_sort(A):
	'''insert sort'''
	pass



def choise_sort(A):
	'''choise sort'''
	pass



def bubble_sort(A):
	'''bubble sort'''
	A_prev=[]
	n=0
	if A==A_prev:
		return n
	else:
		A_prev=A
		for k in range(len(A)-1):
			for i in range(len(A)-1):
				if A[i]>A[i+1]:
					A[i], A[i+1]=A[i+1],A[i]
					n+=1
	return(n)





def my_test(function):
	print('Testing', function.__doc__)
	print('testcase #1: ', end='')
	test_input=[9,8,7,6,5,4,3,2,1,0]
	control_case=45
	function_output=function(test_input)
	print ( 'Ok' if function_output==control_case else 'Fail', function_output) 	            

	print('testcase #2: ', end='')
	test_input=[5,0,1,2,3,4,5]
	control_case=5
	function_output=function(test_input)
	print ('Ok' if function_output==control_case else 'Fail', function_output) 	


if __name__ == '__main__':
	my_test(insert_sort) 
	my_test(choise_sort) 
	my_test(bubble_sort) 


