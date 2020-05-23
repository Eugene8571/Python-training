

'''
N=int(input())
A=str(input()).split(' ')
print(A)
'''


def knights_island(N,s):
	N=int(N)
	s=s.replace(' ','')
	print(N)
	print(s)

	k=0

	var='1'
	s=s+var
	for i in range(1,N):
		if (var[i-1]==0 and s[i]==0) or (var[i-1]==1 and s[i]==1):
			var+='1'
		else: 
			var+='0'
	print(var)
	if var==s:
		return var[:-1].count('1')








'''

(var[i-1]==0 and s[i]==1) or (var[i-1]==1 and s[i]==0):

'''





N='4'
s='0 1 0 1'
print(knights_island(N,s))