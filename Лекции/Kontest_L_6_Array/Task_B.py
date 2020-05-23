def long(a):
	A=[int(n) for n in a.split(' ')]
	if len(A) != 3:
		return 0
	vklad=x=A[0]
	p=A[1]
	y=A[2]
	n=0


	while vklad<=y and n<100:

		vklad = x+x*p/100
		#print(vklad)
		x=vklad*100//1/100
		#print(x)
		n+=1
	return n

21321
#t=long(str(input()))
#print(t)





















def my_test(function):
	print('Тест ', function.__doc__)
	print('testcase #1: ', end='')
	test_case='10 50 50'
	control_case=4
	test_try=function(test_case)
	print(test_try)
	print ('Ok' if test_try==control_case else 'Fail') 	            

if __name__ == '__main__':
	my_test(long)