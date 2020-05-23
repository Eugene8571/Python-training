def isMatch(s, p):
    if s == p:
        return 'true'
    if s == [] and p != []:
        return 'false1'
    sub = s[0]

   for i in range(1, len(s)):
        while p[i] == '*' and\
        (p[i-1]   :
            if sub[i-1] != s[i-1] or p[i-1] != '.'):

        if s[i] == p[i] or p[i] == '.':
            sub += s[i]
        if p(i)








        if p[i] == '*' and \
            
        if len(p) == 0:
            return 'false3'
        if p[len(p) - 1] != '*' and len(p) <= i:
            return 'false4'

        elif p[i] == '*' \
        and (p[len(sub)-1] == s[i - 1] or p[len(sub)-1] == '.'):
            while len(sub) < i:
                sub += sub[i - 1]
        else:
            return 'false5'
    return 'true'


print(isMatch('aa','a*'))
print(isMatch('aa','.*'))
print(isMatch('aab','c*a*b*'))