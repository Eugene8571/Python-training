
def count_digit(s):
	A=[str(i) for i in s.split(' ')]
	n=0
	for i in str(A[1]):
		if i==str(A[0]):
			n+=1
	return n


print(count_digit(str(input())))


#n=str(A[1]).count(str(A[0]))
#print (count_digit('3 1323533'))
print (count_digit('0 0000000'))