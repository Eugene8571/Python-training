#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    
    r=d=l=u=0
    while r+d+l+u<2:
        while wall_is_on_the_right() is False and wall_is_above() is True and r+d+l+u<2:
            move_right()
            if wall_is_on_the_right() is True:
                r=1
        while wall_is_beneath() is False and wall_is_on_the_right() is True and r+d+l+u<2:
            move_down()
            if wall_is_beneath() is True:
                d=1
        while wall_is_on_the_left() is False and wall_is_beneath() is True and r+d+l+u<2:
            move_left()
            if wall_is_on_the_left() is True:
                l=1
        while wall_is_above() is False and wall_is_on_the_left() is True and r+d+l+u<2:
            move_up()
            if wall_is_above() is True:
                u=1

            
        
if __name__ == '__main__':
    run_tasks()
