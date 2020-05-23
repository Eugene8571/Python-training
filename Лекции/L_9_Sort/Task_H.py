
'''

def fig(N, i):
    S=str(N)
    L=len(S)
    if L<i+1:
        return 0
    return int(S[L-1-i])




def flip_sort():
    length=int(input())
    s=str(input())

    N=int(length)
    A=[int(i) for i in s.split(' ')]
    
    L=len(str(max(A)))
    for top in range(1,N):
        i=top
        while i>0 and fig(A[i-1],0) > fig(A[i],0):
            
            A[i], A[i-1]=A[i-1],A[i]
            i-=1

    for m in range(1,L):
        for top in range(1,N):
            i=top
            while i>0 and fig(A[i-1],m) > fig(A[i],m):
                if fig(A[i-1],m-1) == fig(A[i],m-1):
                    A[i], A[i-1]=A[i-1],A[i]
                i-=1    
    

        


    return ' '.join(str(i) for i in A)




print(flip_sort())


'''




def fig(N, i):
    S=str(N)
    L=len(S)
    if L<i+1:
        return 0
    return int(S[L-1-i])




def flip_sort(length,s):

    N=int(length)
    A=[int(i) for i in s.split(' ')]
    print(N)
    print(A)
    
    L=len(str(max(A)))
    for top in range(1,N):
        i=top
        while i>0 and fig(A[i-1],0) > fig(A[i],0):
            
            A[i], A[i-1]=A[i-1],A[i]
            i-=1

    for m in range(1,L):
        for top in range(1,N):
            i=top
            while i>0 and fig(A[i-1],m) > fig(A[i],m):
                if fig(A[i-1],m-1) == fig(A[i],m-1):
                    A[i], A[i-1]=A[i-1],A[i]
                i-=1    
    

        


    return A




print(flip_sort('6','5 23 843 3 43 123'))








