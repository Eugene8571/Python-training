def average():
	A=[]
	while 0 not in A:
		A.append(int(input()))

	return round(sum(A)/(len(A)-1), 2)

print(average())









def av_test():
	A=[4,8,5,0]
	return round(sum(A)/(len(A)-1), 2)

print(av_test())