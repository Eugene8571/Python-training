def isValid(s):
    stack = []
    for p in s:
        if p not in '(){}[]':
            continue
        if p in '[({':
            stack += p
        if p in '])}':
            if stack == []:
                return False
            left = stack.pop()
            if left == '(' and  p != ')':
                return False
            if left == '{' and  p != '}':
                return False
            if left == '[' and  p != ']':
                return False

   
    return True if stack == [] else False

print(isValid('((){}[1])'))
print(isValid('(()){)}[{}]}'))
print(isValid('(]'))
print(isValid('([)]'))


