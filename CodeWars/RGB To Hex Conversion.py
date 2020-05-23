def rgb(a, b, c):
	B=[a,b,c]
	for i in range(3):
		if B[i] < 0:
			B[i]=0
		if B[i] > 255:
			B[i]=255
		B[i]=str(hex(B[i]))[2:]
		if len(B[i])==1:
			B[i]='0'+B[i]




	
	return ''.join(str(x).upper() for x in B)



#print(rgb(0,0,254))


from my_test import test
test(rgb, [255,255,255], 'FFFFFF')
test(rgb, [0,0,0], '000000')
test(rgb, [-20,275,125], '00FF7D')
test(rgb, [0,0,0], '000000')
test(rgb, [0,0,0], '000000')


