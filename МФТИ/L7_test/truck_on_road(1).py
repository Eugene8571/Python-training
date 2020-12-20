def delivery():
	'''
	empty_truck_weight=int(input())
	truck_platform_height=int(input())
	piano_weight=int(input())
	piano_height=int(input())
	fridge_weight=int(input())
	fridge_height=int(input())
	maximum_weight=int(input())
	maximum_height=int(input())
	'''
	empty_truck_weight=1
	truck_platform_height=1
	piano_weight=5
	piano_height=5
	fridge_weight=5
	fridge_height=10
	maximum_weight=11
	maximum_height=10



	if piano_weight>=fridge_weight and piano_height>=fridge_height:
		if piano_weight+empty_truck_weight<=maximum_weight \
		and piano_height+truck_platform_height<=maximum_height:
			return 'YES'
	#print (piano_weight, fridge_weight, piano_height, fridge_height)
	#print(piano_height, truck_platform_height, maximum_height)


	if piano_weight<=fridge_weight and piano_height<=fridge_height:
		if fridge_weight+empty_truck_weight<=maximum_weight \
		and fridge_height+truck_platform_height<=maximum_height:
			return 'YES'
	#print(fridge_weight, empty_truck_weight, maximum_weight)
	#print(fridge_height, truck_platform_height, maximum_height)

	h=min((truck_platform_height+piano_height), (truck_platform_height+fridge_height))
	m=min((empty_truck_weight+piano_weight), (empty_truck_weight+fridge_weight))

	print (h, maximum_height, m , maximum_weight)

	if h<=maximum_height and m<=maximum_weight:
		return 'YES'
	return 'NO'

print(delivery())