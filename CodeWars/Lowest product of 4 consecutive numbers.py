def lowest_product(S):
    print(S)
    if len(S)<4:
        return "Number is too small"

    product=10000000000
    for i in range(3,len(S)):
        
        loc_min: int=int(S[i-3])*int(S[i-2])*int(S[i-1])*int(S[i])
        if product>loc_min:
            product=loc_min
    return product


print(lowest_product("123456789"))



'''
Test.assert_equals(lowest_product(),24); 
Test.assert_equals(lowest_product("2345611117899"),1);
Test.assert_equals(lowest_product("2305611117899"),0);
Test.assert_equals(lowest_product("333"),"Number is too small");
Test.assert_equals(lowest_product("1234111"),4,"Numbers should be consecutives");
'''