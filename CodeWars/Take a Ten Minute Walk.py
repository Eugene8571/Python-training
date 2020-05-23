def isValidWalk(walk):
	s=''.join(walk)
	if s.count('n')==s.count('s') and s.count('w')==s.count('e'):
		return 'true'
	return 'false'


	

print(isValidWalk(['n', 's', 'w', 'e', 'e']))









#    ['n', 's', 'w', 'e']