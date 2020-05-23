def anagrams(palette, A):
	B=[]
	Palette=[i for i in palette]
	for word in A:
		Word=[i for i in word]
		if sorted(Word)==sorted(Palette):
			B.append(word)
	return B

















from my_test import test
test(anagrams, ['abba', ['aabb', 'abcd', 'bbaa', 'dada']], ['aabb', 'bbaa'])
test(anagrams, ['racer', ['crazer', 'carer', 'racar', 'caers', 'racer']], ['carer', 'racer'])