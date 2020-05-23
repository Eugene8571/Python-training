
def to_camel_case(s):
    i = 0
    while i < len(s):
        if s[i-1].isalpha() == False and s[i].isalpha():
            s = s.replace(s[i-1] + s[i], s[i].capitalize())
        i += 1
    return s

print(to_camel_case("the-stealth-warrior"))