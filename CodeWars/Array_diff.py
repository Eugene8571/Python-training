def arrey_diff(a,b):
	d=[]
	for x in a:
		if x not in b:
			d.append(x)
	return d



print(arrey_diff([1,2,2,2,34,4,5],[2,4]))