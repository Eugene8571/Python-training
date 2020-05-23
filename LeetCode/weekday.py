# 


# print(dayOfTheWeek(day = 31, month = 8, year = 2019))

# 0

# Monday

# 1

# Tuesday

# 2

# Wednesday

# 3

# Thursday

# 4

# Friday

# 5

# Saturday

# 6

# Sunday
def dayOfTheWeek(day: int, month: int, year: int) -> str:

    import datetime
    days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    d = datetime.date(year,month,day)
    return days_list[datetime.datetime.today().weekday()]

print(dayOfTheWeek(day=8, month=11, year=2019))