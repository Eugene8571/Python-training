def strip_url_params(url, params_to_strip = []):
    A=url[16:]
    B=[str(i) for i in A.split('=')]
    for i in range(len(B)):
    	for k in range(1, )






    
    print(B)
    return (B) 
    







def my_test(function):
	print('Testing ', function.__doc__)

	print('Test case #1: ')#, end='')
	test_input_url='www.codewars.com?a=1&b=2&a=2'
	test_input_pts=[]
	correct_output=''
	actual_output=strip_url_params(test_input_url, test_input_pts)
	print('OK' if actual_output==correct_output else 'Fail')
	



if __name__=='__main__':
	my_test(strip_url_params)