import string
from codecs import encode

def rot13(message):
	alfabet='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz\
	ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
	alfabet+=alfabet
	decoded=''
	for a in message:
		#print(alfabet.index('t'))
		#print(alfabet[19+13])
		if a in alfabet:
			decoded+=alfabet[alfabet.index(a)+13]
		else: decoded+=a

	return decoded




from my_test import test
test(rot13,"test","grfg")
test(rot13,"Test","Grfg")