def cat_mouse(map_, moves):
    x1=map_[:-18]
    x2=map_[9:-9]
    x3=map_[18:]




    if 'C' in map_:
        maus_x=map_.index('C')
    else:
        return print('boring without two animals')
        

    cat_x=map_.index('C')
    #print(cat_x)
    if cat_x < 9:
    	cat_y=1
    elif 8<cat_x<18:
    	cat_y=2
    	cat_x-=9
    elif cat_x > 17:
    	cat_y=3
    	cat_x-=18
    else:
    	print('boring without two animals')



    if 'm' in map_:
        maus_x=map_.index('m')
    else:
        return print('boring without two animals')
        
    if maus_x < 11:
    	maus_y=1
    elif 11<maus_x<20:
    	maus_y=2
    	maus_x-=11
    elif maus_x > 19:
    	maus_y=3
    	maus_x-=20
    else:
    	print('boring without two animals')


    if abs(cat_x-maus_x)+abs(cat_y-maus_y)<=moves:
    	print("Caught!")
    else:
    	print("Escaped!")





map_ = '''\
..C......
.........
....m....'''

for i in map_:
    print(i)
#Test.assert_equals(cat_mouse(map_, 5), 'Caught!')





#map_ = '..C...................m....'

cat_mouse(map_, 5)















#Test.assert_equals(cat_mouse(map_, 5), 'Caught!')

