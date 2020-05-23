def roman_to_int(S):
    rom_dict = {1: 'I', 
                5: 'V', 4:'IV', 
                10: 'X', 9:'IX',
                50: 'L', 40:'XL',
                100: 'C', 90:'XC',
                500: 'D', 400:'CD',
                1000: 'M', 900:'DM'}
    K = [key for key in rom_dict.keys()]
    print(K)
    print(rom_dict.keys())
    num = 0

    




roman_to_int('MCMXCIV') #1994
