def create_phone_number(n):
    A=[*n]
    TN='('+str(A[0])+str(A[1])+str(A[2])+') '+str(A[3])+str(A[4])+str(A[5])+'-'+str(A[6])+str(A[7])+str(A[8])+str(A[9])
    return(TN)

phone_number=create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])
print(phone_number)

