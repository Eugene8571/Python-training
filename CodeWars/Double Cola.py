def who_is_next(names, n):
    for i in range(n):
        names.append(names[0])
        names.append(names[0])
        names = names[1:]
    return names.pop()


st_test = 52
print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], st_test))
# print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 52) == "Penny")
# print(who_is_next(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951) == "Leonard")


def who_is_next_01(names, n):
    if n <= len(names):
        return names[n-1]
    m = len(names)
    sum_ = m
    while sum_ < n:
         m *= 2
         sum_ += m
    
    step = m / len(names)

    prev = sum_ - m 
    part = 0
    step_N = 0
    while prev + part < n:
        step_N += 1
        part = step * step_N

    return names[step_N - 1] # , sum_, sum_ - m, step, part, step_N


print(who_is_next_01(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], st_test))
