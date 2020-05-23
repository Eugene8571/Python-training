def words_and_numbers(S):
    A = [i for i in S.split()]
    B = [''] * len(A)
    for word in A:
        n = ''
        for simbol in word:
            if simbol.isdigit():
                n += simbol
        B[int(n) - 1] = word

    
    return ' '.join(B)


print(words_and_numbers("4of Fo1r pe6ople g3ood th5e the2"))