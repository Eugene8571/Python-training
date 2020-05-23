def likes(names):

	d={
		0: 'no one likes this',
		1: '{} likes this',
		2: '{} and {} like this',
		3: '{}, {} and {} like this',
		4: '{}, {} and {others} others like this'
	}

	return d[min(4, len(names))].format(*names, others = len(names)-2)








print(likes([]))
print(likes(["Peter"]))
print(likes(["Peter", 'Artur']))
print(likes(["Peter", 'Artur', 'Yorick']))
print(likes(["Peter", 'Artur', 'Yorick', 'Dante']))
