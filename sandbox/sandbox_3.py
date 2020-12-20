def mix(s1, s2):
    def split_n_group(s):
        arr = []
        used = ''
        for sim in s:
            # print(sim)
            if sim not in used:
                n = s.count(sim)
                if n > 1:
                    if sim * n not in arr:
                        arr.append(sim*n)
        return arr
    arr1 = split_n_group(s1)
    arr2 = split_n_group(s2)
    united = arr1 + arr2
    print(united)
    for char in united:
        if not char.isalpha() or not char.islower():
            united.pop(united.index(char))
    print(united)
    


print(mix("A generation must confront the looming ", "codewarrs") == "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")