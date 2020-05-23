def cat_mouse(map_, moves):
	C_y=C_x=m_y=m_x=0
	if 'C' not in map_ or 'm' not in map_:
		return ("boring without two animals")
		
	if map_.index('C') <= 10:
		C_y=1 
		C_x=map_.index('C')
	elif 10<map_.index('C') <= 21:
		C_y=2
		C_x=map_.index('C')-11
	elif 21<map_.index('C') <= 31:
		C_y=3
		C_x=map_.index('C')-22
	

	if map_.index('m') <= 10:
		m_y=1
		m_x=map_.index('m') 
	elif 10<map_.index('m') <= 21:
		m_y=2
		m_x=map_.index('m')-11 
	elif 21<map_.index('m') <= 31:
		m_y=3
		m_x=map_.index('m')-22

	
	if abs(C_x-m_x)+abs(C_y-m_y)<moves:
		return ('Caught!')
	elif abs(C_x-m_x)+abs(C_y-m_y)>=moves:
		return ("Escaped!")

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