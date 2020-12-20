s=str(input())
n=int(input())

def degree_of(s,n):
	if n==0:
		return s
	if n>0:
		return s*n
	# n<0
	part=''
	for i in range(len(s)):
		part+=s[i]
		if part*(-n)==s:
			return part
	return 'NO SOLUTION'

print(degree_of(s,n))

'''
print(degree_of('abc',3))
print(degree_of('abcdabcd',-2))
print(degree_of('abcd',-4))
'''