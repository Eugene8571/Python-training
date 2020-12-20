#A=str(input())

#A='1 23'
A='f0 0f'

B=[int(i, 16) for i in A.split(' ')]

S = B[0] ^ B[1]
print(hex(S)[2:]) 

