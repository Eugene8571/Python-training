def check_string(str0, str1, token):
    L = len(str0)


    def check_token_in_place(str0, i, token, str1):
        for x in range(len(str0)-i):
            # print(f'{i=}', f'{str0[x:]=}',  f'{x=}', )

            if str0[:i] + token + str0[x:] == str1\
            or str0[:i] + token == str1:
                return True



    for i in range(L):
        if check_token_in_place(str0, i, token, str1):
            return True

    return False


str0 = '00000000000000123000000000000000'
token = 'a'
str1 = '00000000000000a000000000000000'

print(check_string(str0, str1, token)==True)

str0 = '00000w000000000123000000000000000'
token = 'a'
str1 = '00000000000000a000000000000000'

print(f'{check_string(str0, str1, token)==False}')


str0 = '123000000000000000'
token = ''
str1 = '00000000000000a000000000000000'

print(f'{check_string(str0, str1, token)==False}')

str0 = '123000000000000000'
token = 'a'
str1 = 'a000000000000000'

print(f'{check_string(str0, str1, token)==True}')

str0 = '1000000000000000'
token = 'a'
str1 = 'a000000000000000'

print(f'{check_string(str0, str1, token)==True}')

str0 = '0'
token = '1'
str1 = '1'

print(f'{check_string(str0, str1, token)==True}')

str0 = 'q0'
token = '1'
str1 = 'q1'

print(f'{check_string(str0, str1, token)==True}')

str0 = 'q00'
token = '1'
str1 = 'q1'

print(f'{check_string(str0, str1, token)==True}')





