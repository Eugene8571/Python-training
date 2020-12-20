def delivery():
	truck_m=int(input())
	truck_h=int(input())
	piano_m=int(input())
	piano_h=int(input())
	fridge_m=int(input())
	fridge_h=int(input())
	max_m=int(input())
	max_h=int(input())

	truck_m=1
	truck_h=1
	piano_m=5
	piano_h=5
	fridge_m=5
	fridge_h=10
	max_m=11
	max_h=10

	# road #1 piano / max_h

	m=truck_m+piano_m+fridge_m

	
	if piano_h+truck_h<=max_h and fridge_h+truck_h<=max_h:
		m=m-piano_m
	


	if m<=max_m:
		h=


print(delivery())