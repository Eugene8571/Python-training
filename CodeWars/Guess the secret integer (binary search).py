

# def binary_search(low, high, guess):
#     def func(low, high, guess):
#         if low == high:
#             return low
#         if low == guess[2]:
#             return low
#         if high == guess[2]:
#             return high
#         mid = low + (high - low) // 2
#         # print('mid '+str(mid))
#         if mid == guess[2]:
#             return mid
#         else:
#             if mid > guess[2]:
#                 high = mid
#                 # print('mid > guess[2] ' + str(mid))
#             if mid < guess[2]:
#                 low = mid
#                 # print('mid < guess[2] ' + str(mid))
#             func(low, high, guess)

#     print(func(low, high, guess))



# guess = (1,1,1)
# binary_search(1,1,guess)
# # , 1, 'Testing when low == high')
# guess = (1,10,1)
# binary_search(1,10,guess)
# # , 1, 'Testing edge case')
# guess = (1,10,10)
# binary_search(1,10,guess)
# # , 10, 'Testing edge case')


# guess = (1,10,3)
# binary_search(1,10,guess)
# , 3, 'Couple of small tests')
# guess = (1,10,8)
# binary_search(1,10,guess)
# # , 8, 'Couple of small tests')
# guess = (1,10,6)
# binary_search(1,10,guess)
# # , 6, 'Couple of small tests')

# guess = (1,10**5,2314)
# binary_search(1,10**5,guess)
# # , 2314, 'Couple of bigger tests')
# guess = (1,10**6,1111)
# binary_search(1,10**6,guess)
# # , 1111, 'Couple of bigger tests')
# guess = (1,10**6,6698)
# binary_search(1,10**6,guess)
# # , 6698, 'Couple of bigger tests')


# a = 17/5 - 9/10
# b = 8//3 + 8//-3
# print( a ," ", b )


# def fun01(my_args):
#     for name,value in enumerate(my_args):
#         print('{0} is an {1}'.format(name, value))

  
# def fun02(*my_args):
#     for name,value in enumerate(my_args):
#         print('{0} is an {1}'.format(name, value))

  
# def fun03(**my_args):
#     for name,value in enumerate(my_args):
#         print('{0} is an {1}'.format(name, value))


# # fun01(caption='acme', length=523, units='mm')  # a
# # fun02(caption='acme', length=523, units='mm')  # b
# fun03(caption='acme', length=523, units='mm')  # c

class A:
    @classmethod
    def foo(cls):
        print("bar");

    def bar(self):
        print("foo");

a=A();

a.foo()  # 1
A.foo()  # 2
a.bar()  # 3
# A.bar()  # 4

print(19%7)