def ascii_sort(s):
	#s=s.replace(' ','')
	s=s[:-(len(s)-s.index('.'))]	
	S=[str(i) for i in s]
	


	N=len(S)
	for top in range(1, N):
		k = top
		while k > 0 and S[k-1] > S[k]:
			S[k], S[k-1] = S[k-1], S[k]
			k-=1
			


	return(''.join(S) + '.')


print(ascii_sort(str(input())))








print('ok' if ascii_sort('qwe Rty5, yu! Mama.6665556rr')=='!,5MRaaemqtuwyy.' else 'Fail')


'''

	print(s)
	S=s.strip(' ')
	print(S)
	S[:-(len(S)-S.index('.'))]
	print(S)

#print('a' if 'a'>='!' else '!')

print()













'''