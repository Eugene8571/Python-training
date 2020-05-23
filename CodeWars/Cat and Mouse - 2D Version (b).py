def cat_mouse(map_, moves):

	if 'C' not in map_ or 'm' not in map_:
		return ("boring without two animals")

	for row, line in enumerate(map_.splitlines()):
		if 'C' in line:
			cat = row, line.index('C')
		if 'm' in line:
			mouse = row, line.index('m')

	distance = abs(cat[0] - mouse[0]) + abs(cat[1]-mouse[1])

	return 'Caught!' if distance <= moves else "Escaped!"

























	
		#return ('Caught!')
	
		#return ("Escaped!")

def my_test(function):
	print('Testing', function.__doc__ if function.__doc__!=None else '------------')
	print('testcase #1: ', end='')
	map_ = '''\
	..C......
	.........
	....m....'''
	moves=5
	control_case='Caught!'
	function_output=function(map_, moves)
	print ( 'Ok' if function_output==control_case else 'Fail', function_output) 	

	print('testcase #2: ', end='')
	map_='''\
	.C.......
	.........
	......m..'''
	moves=5
	control_case='Escaped!'
	function_output=function(map_, moves)
	print ( 'Ok' if function_output==control_case else 'Fail', function_output) 

	print('testcase #3: ', end='')
	map_='''\
	..C......
	.........
	.........'''
	moves=5
	control_case='boring without two animals'
	function_output=function(map_, moves)
	print ( 'Ok' if function_output==control_case else 'Fail', function_output) 

	print('testcase #4: ', end='')
	map_='''\
	..C......
	.........
	......m..'''
	moves=5
	control_case='Escaped!'
	function_output=function(map_, moves)
	print ( 'Ok' if function_output==control_case else 'Fail', function_output) 

if __name__ == '__main__':
	my_test(cat_mouse) 