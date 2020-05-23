

def longest_consec(arr, k):
    if k > len(arr) or k <= 0 or len(arr) == 0:
        return ''
    res = ''
    sub = []
    for i in range(len(arr) +1 - k):
        print(i)
        sub.append(''.join(arr[i:i+k]))
    for line in sub:
        if len(line) > len(res):
            res = line 
    print(res)
    return res



print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) == "abigailtheta")
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) == "oocccffuucccjjjkkkjyyyeehh")
print(longest_consec([], 3) == "")
print(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) == "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
print(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2) == "wlwsasphmxxowiaxujylentrklctozmymu")
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) == "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15) == "")
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0) == "")