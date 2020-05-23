def longestPalindrome_a(s):
    if len(s) <= 1 or (len(s) == 2 and s[0] == s[1]):
        return s
    if len(s) == 2 and s[0] != s[1]:
        return s[0]

    # len(s) >= 3
    A = []
    for x in s:
        A.append(x)
        A.append('#')
    A.pop()
    
    pal = []
    loc_pal = []
    for i in range(1, len(A)):
        j = 1
        while i - j - 1 > 0 and i + j + 1 < len(A):
            if A[i - j] == A[i + 1 + j]:
                print(j)
                j += 1
            else:
                print(loc_pal)
                loc_pal = A[i-j - 1:i+j+1 + 1 - 1]
                break
        if len(pal) < len(loc_pal):
            pal = loc_pal
        
    pal.extend(pal[::-1])
    s = ''.join(i for i in pal)
    s = s.replace('#', '')
    return s


def longestPalindrome_b(s):
    if len(s) <= 1 or (len(s) == 2 and s[0] == s[1]):
        return s
    if len(s) == 2 and s[0] != s[1]:
        return s[0]

    Line = ''
    for char in s:
        Line += char + '#'
    #print(Line)

    max_move = 0
    palindrom = ''
    for i in range(1, len(Line)-1):
        #print(Line[i-1], Line[i+1])
        move = 0
        while i - 1 - move > 0 and i + 1 + move < len(Line) - 1:
            #print(Line[i-1-move], Line[i+1+move], move, palindrom)
            if Line[i-1-move] == Line[i+1+move]:
                move += 1
            else: break
        if max_move < move:
            max_move = move
            palindrom = Line[i-move-1:i+1+move+1]

    palindrom = palindrom.replace('#', '')
                
    return palindrom


def longestPalindrome_c(s):
    S = ''
    for x in s:
        S += x + '#'

    max_step = 0
    i_ = 0
    for i in range(1, len(S)):
        step = 0
        while i - step >= 0 and i + step <= len(S) - 1:
            if S[i - step] != S[i + step]:
                break
            step += 1

        if step - 1 > max_step:
            max_step = step - 1
            i_ = i

    return S[i_ - max_step: i_ + max_step + 1].replace('#', '')


print(longestPalindrome_c('2227ccc22'))
#print(longestPalindrome("kztakrekvefgcherscfcqcsmkraimfwwfuvehpxd"))
print(longestPalindrome_c('1eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee5') == 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
