def db_sort(arr):
	I=[]
	S=[]
	for x in range(len(arr)):
		if type(arr[x]) is int:
			I.append(arr[x])
		else:
			S.append(arr[x])

	I.sort()
	#print(I)
	S.sort()
	#print(S)
	I.extend(S)
	#print(I)
	return(I)



A=db_sort([1,2, 'e', 'dgdf', 'a', 10,5])
print(A)

#print(type([1,2,10,5]))