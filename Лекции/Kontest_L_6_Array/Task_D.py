def input_data():
	a=''
	S=[]
	t=''
	for i in range(1000):
		t=str(input())
		if t=='#':
			break
		elif len(t)>5:
			a=t
			a=a.strip()
			S=[int(i) for i in a.split(' ')]
			S[0], S[len(S)-1]=S[len(S)-1], S[0]
			return (print(S))
		else:
			a+=' '	
			a+=t

	a=a.strip()

	S=[int(i) for i in a.split(' ')]
	


	S=input_data()


	S_sum=sum(S)
	S_min=min(S)
	S_med=round((S_sum/len(S)), 3)
	S_sum_mod=0

	for n in range(int(len(S)/3)):
		S_sum_mod += (S[3*n]+S[3*n+1]+S[3*n+2]) % (S[3*n+2])


	return (print(S_med, max(S), min(S), S_sum_mod))  


input_data()

		
