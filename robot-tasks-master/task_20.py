#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    
    move_right()
    
    for i in range(6):
    
        while wall_is_on_the_right() is False:
            fill_cell()
            move_right()
        
        move_left()
        move_down()
    
        while wall_is_on_the_left() is False:
            fill_cell()
            move_left()
    
        move_right()
        move_down()

if __name__ == '__main__':
    run_tasks()
