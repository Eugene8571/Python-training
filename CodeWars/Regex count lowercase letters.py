def lowercase_count(strng):
    n=0
    for l in strng:
        
        if l.islower() is True:
            n+=1
            print(l)
    return (n)


K=lowercase_count("abcABC123")
print (K)