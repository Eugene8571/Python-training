
S=-1
loc_max=0

while S!=0:
	S=int(input())
	if loc_max<S:
		loc_max=S
		n=1
	elif loc_max==S:
		n+=1
print(n)

