#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    
    s=1
    
    move_right()
    
    while wall_is_on_the_right() is False or wall_is_beneath() is False:
        if wall_is_above() is False:
            while wall_is_above() is False:
                move_up()
                fill_cell()
        if wall_is_beneath() is False:
            while wall_is_beneath() is False:
                move_down()
        move_right()
        s+=1
        
    if wall_is_above() is False:
            while wall_is_above() is False:
                move_up()
                fill_cell()
    if wall_is_beneath() is False:
            while wall_is_beneath() is False:
                move_down() 
                
    move_left(n=s)

if __name__ == '__main__':
    run_tasks()
