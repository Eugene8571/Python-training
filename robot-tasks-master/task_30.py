#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    
        
        
    a=1
    b=1
    c=1
    
    
    while wall_is_on_the_right() is False:
        move_right()
        c+=1
    while wall_is_on_the_left() is False:
        move_left()
    
    while wall_is_beneath() is False:
        while wall_is_on_the_right() is False:
            if a!=b and a+b!=c+1:
                fill_cell()
            move_right()
            a+=1
        c==a
        if a!=b and a+b!=c+1:
            fill_cell()
        if wall_is_beneath() is False:
            move_down()
            b+=1
        while wall_is_on_the_left() is False:
            if a!=b and a+b!=c+1:
                fill_cell()
            move_left()
            a-=1
        if a!=b and a+b!=c+1:
            fill_cell()
        if wall_is_beneath() is False:
            move_down()
            b+=1

    if cell_is_filled() is False:
        while wall_is_on_the_right() is False:
            if a!=b and a+b!=c+1:
                fill_cell()
            move_right()
            a+=1
        if a!=b and a+b!=c+1:
            fill_cell()
        while wall_is_on_the_left() is False:
            move_left()
            a-=1
    
    
    



if __name__ == '__main__':
    run_tasks()
