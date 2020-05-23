def function(n):
	b=bin(n)
	s=str(b)
	s=s[2:]
	print(s)
	short=s.replace('0', '')
	if len(s)%2==1 and len(s)-len(short)==1:
		return True
	return False
	
	















print(function(13))