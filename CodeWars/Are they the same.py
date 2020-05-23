# def comp(a,b):
#     if b == [] and a != []:
#         print('[]')
#         return False
#     if None in a:
#         return False
#     for i in a:
#         print(i, i**2, b)
#         if i**2 not in b:
#             print(i**2, ' not in ', b)
#             return False
#         b.remove(i**2)
#     return True

def comp(a,b):
    try:
        return sorted([i**2 for i in a]) == sorted(b)
    except:
        return False




a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a,b)==True)

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [11*12, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a,b)==False)

a = [120, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a,b)==False)

a = [48, 58, 55, 4, 44, 94, 4, 58]
b = [2304, 3364, 3025, 16, 1936, 8836, 17, 3364]
print(comp(a,b)==False)


a = [19, 19, 19, 121, 144, 161, 144, 11, 1008]
b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
print(comp(a,b)==False)


