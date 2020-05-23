'''
def parantheses_check(s):
	cnt=0
	for char in s:
		if char=='(':
			cnt+=1
		if char==')':
			cnt-=1
		if cnt<0:
			return False

	return True if cnt==0 else False

'''


def parantheses_check(s):
    cnt = 0
    for v in s:
        if v == '(':
            cnt += 1
        if v == ')':
            cnt -= 1
        if cnt < 0:
            return False
    
    return True if cnt == 0 else False






from my_test import test
test(parantheses_check, '()', True)
test(parantheses_check, '((()())))()', False)
test(parantheses_check, '(((())))()12312331', True)
test(parantheses_check, '()))((()aaaaaaaaaaaaa', False)
