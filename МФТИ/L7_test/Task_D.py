def max_even():
	A=[]
	while 0 not in A:
		A.append(int(input()))


	loc_max=0
	for x in A:
		if x%2==0 and x>loc_max:
			loc_max=x

	return loc_max

print(max_even())