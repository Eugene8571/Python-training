def likes(names):
	L=' like this'
	if len(names)==0:
		return 'no one'+' likes this'
	elif len(names)==1:
		return names[0]+' likes this'
	elif len(names)==2:
		return names[0]+' and '+names[1]+L
	elif len(names)==3:
		return names[0]+', '+names[1]+' and '+names[2]+L
	else:
		return names[0]+', '+names[1]+' and '+str(len(names)-2)+' others'+L










print(likes([]))
print(likes(["Peter"]))