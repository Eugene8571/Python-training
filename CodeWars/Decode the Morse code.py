def decodeMorse(morse_code):
	dictionary={    'A':'.-',     'B':'-...', 
                    'C':'-.-.',   'D':'-..',     'E':'.', 
                    'F':'..-.',   'G':'--.',     'H':'....', 
                    'I':'..',     'J':'.---',    'K':'-.-', 
                    'L':'.-..',   'M':'--',      'N':'-.', 
                    'O':'---',    'P':'.--.',    'Q':'--.-', 
                    'R':'.-.',    'S':'...',     'T':'-', 
                    'U':'..-',    'V':'...-',    'W':'.--', 
                    'X':'-..-',   'Y':'-.--',    'Z':'--..', 
                    '1':'.----',  '2':'..---',   '3':'...--', 
                    '4':'....-',  '5':'.....',   '6':'-....', 
                    '7':'--...',  '8':'---..',   '9':'----.', 
                    '0':'-----',  ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.',   '-':'-....-', 
                    '(':'-.--.',  ')':'-.--.-',  '!':'-.-.--',
                    'SOS':'...---...'
                    } 
	MORSE_CODE=[str(i) for i in morse_code.split(' ')]
	readable=''
	for group in MORSE_CODE:

		for simbol, dots in dictionary.items():
			if group==dots:
				readable+=simbol
		if group=='':
				readable+=' '
	readable=readable.replace('  ', ' ')
	readable=readable.strip()


	return readable




print(decodeMorse('...−−−...  .... . -.--   .--- ..- -.. .')), #'HEY JUDE'
print(decodeMorse('...−−−... -.-.--'))


#morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')