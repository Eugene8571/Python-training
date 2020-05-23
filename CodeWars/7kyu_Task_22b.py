def getCount(inputStr):
    vowels='aeiou'
    #return sum(1 for l in inputStr if l in vowels)
    return sum(a in vowels for a in inputStr)











A=getCount('aeeeebracadabra')
print(A)



'''            print(i) 


or 'e'

  + 'i' + 'o' + 'u'
  or 'i' or 'o' or 'u'
'''