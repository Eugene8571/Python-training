#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    
    x=0
    a=0
    while a==0:
        if wall_is_above() is False and wall_is_beneath() is False:
            a+=1
        while wall_is_on_the_right() is False and wall_is_above() is True:
            if cell_is_filled() is True:
                x+=1
            else:
                fill_cell()
            move_right()
        if wall_is_above() is False and wall_is_beneath() is True:
            while wall_is_above() is False:
                move_up()
                if cell_is_filled() is True:
                    x+=1
                else:
                    fill_cell()
        if wall_is_above() is True and wall_is_beneath() is False:
            while wall_is_beneath() is False:
                move_down()
        if wall_is_on_the_right() is False:
            move_right()
        if wall_is_above() is False and wall_is_beneath() is False:
            a+=1
    
    mov('ax', x)


if __name__ == '__main__':
    run_tasks()
