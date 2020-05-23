# right прямоугольный
# acute острый
# obtuse тупой
# impossible

def triangle_typy():
	
	a=int(input())
	b=int(input())
	c=int(input())
	



	t=[a,b,c]
	t.sort()

	if a>=b+c or b>=a+c or c>=a+b:
		return 'impossible'

	if t[2]**2==t[0]**2+t[1]**2:
		return 'right'

	if t[2]**2 < t[0]**2+t[1]**2:
		return 'acute'

	if t[2]**2 > t[0]**2+t[1]**2:
		return 'obtuse'

print(triangle_typy())