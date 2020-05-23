#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    a=0
    b=0
    
    while wall_is_on_the_right() is False:
        move_right()
        
        if a==b and wall_is_on_the_right() is False:
            fill_cell()
            b+=1
            a=0
        a+=1    
            
        
        
    

if __name__ == '__main__':
    run_tasks()
