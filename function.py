month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def countDays(dd, mm, year):
    if dd > 31:
        return "invalid Day"
    elif mm > 12:
        return "invalid month"
    elif year < 0:
        return "invalid year"
    x = (year - 1) * 365
    if isLeap(year):
        month[2]
    y = int(year / 4) + int(year / 400) - int(year / 100)
    x = x + y
    for z in range(mm):
        x += month[z]
    return x + dd;



print(countDays(23,11,1123))
