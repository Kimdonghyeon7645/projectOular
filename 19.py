#   19. 20세기에서, 매월 1일이 일요일인 경우는 몇 번?
cnt, day = 0, 1
for year in range(1901, 2001):
    for month in range(1, 13):
        if day % 7 == 1:
            cnt += 1
        day += (29 if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0) else 28) \
            if month == 2 else (30 if month in [4, 6, 9, 11] else 31)
print(cnt)
