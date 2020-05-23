def find_outlier(integers):
	check_odd=0
	for i in range(3):
		check_odd+=integers[i]%2
	if check_odd>=2: #return even
		for i in integers:
			if i%2==0:
				return i
	else: #return odd
		for i in integers:
			if i%2==1:
				return i




















print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))