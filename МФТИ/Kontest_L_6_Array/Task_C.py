S=''
for i in range(int(input())):
	S+=str(input())
print (len(S))

n=0
t=0
for i in S:
	if i=='1':
		n+=1
	elif i=='0':
		if n>t:
			t=n
		n=0
print(t)










S=''
for i in range(int(input())):
	S+=str(input())
#print (len(S))

n=0
t=0
for i in S:
	if i=='1':
		n+=1
	elif i=='0':
		t=max(t, n)
		n=0
print(t)

















S=''
for i in range(int(input())):
	S+=str(input())
print (len(S))

n=0
t=0
for i in S:
	if i=='1':
		n+=1
	else:
		if n>t:
			t=n
		n=0
print(t)













S=''
for i in range(int(input())):
	S+=str(input())
#print (len(S))

n=0
t=0
for i in S:
	if i=='1':
		n+=1
	elif n>t:
		t=n
	elif i=='0':
		n=0
print(t)













def my_test(function):
	print('Тест ', function.__doc__)
	print('testcase #1: ', end='')
	test_case='510110'
	control_case=2
	test_try=function(test_case)
	print(test_try)
	print ('Ok' if test_try==control_case else 'Fail') 	            

if __name__ == '__main__':
	my_test(strick)