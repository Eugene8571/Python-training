from statistics import median


def numbers_1():
    for i in range(1, 11):
        print(i)


def numbers_2():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)


def numbers_3():
    n = 0
    for i in range(1, 51):
        n += 1
        if n == 3:
            print(i)
            n = 0


def numbers_4():
    for i in reversed(range(1, 41)):
        if i % 4 == 0:
            print(i)


def numbers_5():
    A = []
    for i in range(1, 101):
        A.append(i)
    for i in range(1, 101):
        for k in range(2, i):
            if i % k == 0:
                if i in A:
                    A.pop(A.index(i))
    for i in A:
        print(i)


def word_0(word):
    print(word)
    n = len(word)
    print('len ', n, ' simbols')
    print('reversed ', word[::-1])
    for i in range(len(word)//2):
        if word[i] != word[::-1][i]:
            print('not palindrome')
            return
    print('palindrome')

# word = '12345asd'
# word_0(word)

# word = '123321'
# word_0(word)

# word = '123a321'
# word_0(word)


def strings_0(string_a, string_b):
    if string_a == string_b:
        print('are equal')
    else:
        print('not equal')
    if (string_a in string_b) or (string_b in string_a):
        print('one string is a substring of the other')
    else:
        print('not a substring')

# string_a = 'asdf'
# string_b = 'asdf'
# strings_0(string_a, string_b)

# string_a = 'asdf'
# string_b = 'asdf12212'
# strings_0(string_a, string_b)

# string_a = 'ghjk'
# string_b = 'asdf12212'
# strings_0(string_a, string_b)


def characters_0(string_0):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    D = {}
    for ch in alphabet:
        D.update({ch: 0})
    for ch in string_0:
        D[ch.lower()] += 1
    print(D)


# string_0 = 'aaasdffff'
# characters_0(string_0)


def numbers_6(A):
    my_list = []
    for i in range(len(A)):
        print(f'{A[i]=}')
        if A[i] == 0:
            break
        my_list.append(A[i])
    av = 0
    md = 0
    n_sorted = []
    if my_list:
        av = sum(my_list)/len(my_list)
        md = median(my_list)
        my_list.sort(reverse=True)
    return my_list, av, md, my_list


# A = [0,22,3]
# print(numbers_6(A))

# A = [4,6,10,0,100]
# print(f'{numbers_6(A)=}')


def words_1(A):
    print('enter word')
    word = str(input())
    if word == 'stop':
        return    
    A.append(word)
    print(A)
    U = []
    for word in A:
        if word not in U:
            U.append(word)
    print('unique ', len(U))
    D = {}
    for word in U:
        D.update({word: A.count(word)})
    print(D)
    words_1(A)


# words_1([])


# import re

# hello = 'Евгений, здравствуйте!'
# name = re.search(r'(.*),', hello)
# if name:
#     print(name.group(1))

# # if (name := re.search(r'(.*),', hello)):
# #     print(name.group(1))

# print(f'{name=}')



def any_lowercase_0(s):
	for c in s:
		if c.islower():
			return True
		else:
			return False



s = 'asadda'
# print(f'{any_lowercase_0(s)}')

def any_lowercase_1(s):
	for c in s:
		flag = c.islower()
	return flag

print(f'{any_lowercase_1(s)}')

for x in range(10):
    pass
var = 'asd'
print(f'{var.islower()=}')

flag = var.islower()
print(f'{flag=}')

