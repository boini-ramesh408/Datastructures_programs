def day_of_week(month, day, year):
    y = year - (14 - month) // 12

    x = y + y // 4 - y // 100 + y // 400
    m = month + 12 * ((14 - month) // 12) - 2
    d = (day + x + (31 * m) / 12) % 7
    return d