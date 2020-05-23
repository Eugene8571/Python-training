def to_bin(I):
	if I<=1:
		return str(I)
	return(str(I%2)+to_bin(I//2))


def bit_counting(I):
	return to_bin(I).count('1')








print(bit_counting(1234))#5