from random import randint


lowest_number = 0
highest_number = 9


in_mind = randint(lowest_number, highest_number)
print('Hello. I have something in mind. Guess what. ')
print('It is a number between ', lowest_number, ' and ', highest_number)
attempts = 5


def function(in_mind, attempts):
    if attempts <= 0:
        print('Fail. No more attempts')
        return
    print('You have ', attempts, ' attempts')
    my_guess = int(input())
    if my_guess == in_mind:
        print('Yes, it was ', in_mind)
        return
    if my_guess > in_mind:
        print('Less')
    if my_guess < in_mind:
        print('More')
    attempts -= 1
    function(in_mind, attempts)


function(in_mind, attempts)
