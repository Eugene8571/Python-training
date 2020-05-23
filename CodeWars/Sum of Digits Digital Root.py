def digital_root(n):
    if n<10:
    	return n
    else:	
	    summ=0
	    for digit in str(n):
	    	summ+=int(digit)
	    return digital_root(summ)

#print(digital_root(5))
print(digital_root(16))
print(digital_root(456))