#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    
    while wall_is_on_the_left() is False or wall_is_beneath() is False:
    
        while wall_is_on_the_right() is False and wall_is_beneath() is True:
            move_right()
        
        while wall_is_on_the_left() is False and wall_is_beneath() is True:
            move_left()
            
        if wall_is_beneath() is False:
            move_down()
                
        
        



if __name__ == '__main__':
    run_tasks()
