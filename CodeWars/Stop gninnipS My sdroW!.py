def spin_words(sentence):
    A=[str(w) for w in sentence.split(' ')]
    
    simbols=':;,.!'
    for i in range(len(A)):
    	if A[i].isalpha()==False:
    		A[i]=A[i][:-1]


    	
    	if len(A[i])>=5:
    		word_arr=[str(s) for s in A[i]]
    		N=len(word_arr)
    		for n in range(N//2):
    			word_arr[n], word_arr[N-n-1] = word_arr[N-n-1], word_arr[n]
    		word_str=''
    		for m in word_arr:
    			word_str+=m
    		A[i]=word_str
			


    return ' '.join(A)









print(spin_words('Welcome home!'))