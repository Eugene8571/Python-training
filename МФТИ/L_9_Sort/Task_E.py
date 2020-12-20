def hooks(a):

	if len(a)%2!=0 or\
	a.count('(')!=a.count(')') or \
	a[0]==')' or\
	a[len(a)-1]=='(' :
		return ('NO')



	return ('YES')

print(hooks(str(input())))




'''
print('ok' if hooks('(()')=='NO' else 'fail')
print('ok' if hooks('(()(')=='NO' else 'fail')
print('ok' if hooks('(()())')=='YES' else 'fail')
print('ok' if hooks(')(')=='NO' else 'fail')
'''