def delivery():
	
	
	truck_m=int(input())
	truck_h=int(input())
	piano_m=int(input())
	piano_h=int(input())
	fridge_m=int(input())
	fridge_h=int(input())
	max_m=int(input())
	max_h=int(input())
	
	'''
	truck_m=1
	truck_h=1
	piano_m=5
	piano_h=10
	fridge_m=5
	fridge_h=10
	max_m=11
	max_h=11
	'''
	'''
	truck_m=1
	truck_h=1
	piano_m=5
	piano_h=10
	fridge_m=5
	fridge_h=10
	max_m=11
	max_h=11
	'''
	'''
	truck_m=1
	truck_h=1
	piano_m=5
	piano_h=10
	fridge_m=5
	fridge_h=7
	max_m=11
	max_h=10
	'''
	m=truck_m+piano_m+fridge_m
	h=truck_m+max(piano_h, fridge_h)


	if m<=max_m and h<=max_h:
		return 'YES'

	if m>max_m and h>max_h:
		return 'NO'

	if m<=max_m and truck_h+fridge_h<=max_h:
		return 'YES'

	if h<=max_h and truck_m+piano_m<=max_m:
		return 'YES'

	return 'NO'




print(delivery())