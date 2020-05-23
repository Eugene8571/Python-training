#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    
    move_right()
    
    for i in range(5):
    
        while wall_is_on_the_right() is False:
            fill_cell()
            move_down()
            fill_cell()
            move_down()
            fill_cell()
            move_right()
            move_up()
            fill_cell()
            move_left()
            move_left()
            fill_cell()
        
            a=0
            while wall_is_on_the_right() is False and a<5:
                move_right()
                a+=1
            if wall_is_on_the_right() is False:
                move_up()    
                
        while wall_is_on_the_left() is False:
            move_left()
        b=0
        while wall_is_beneath() is False and b<3:
            move_down()
            b+=1
        move_right()
        
    move_left()
    move_up(n=2)

        
    
            
            
            

if __name__ == '__main__':
    run_tasks()
