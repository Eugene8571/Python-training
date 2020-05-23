def getCount(inputStr):
    num_vowels=0
    vowels='aeiou'
    for i in inputStr:
        for v in vowels:
        	if i == v:
        		num_vowels += 1

    return num_vowels











A=getCount('aeeeebracadabra')
print(A)



'''            print(i) 


or 'e'

  + 'i' + 'o' + 'u'
  or 'i' or 'o' or 'u'
'''