#   9. a + b + c = 1000 이 되는 피타고라스 수
for a in range(1, 999):
    for b in range(1, 1000-a):
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            print(a*b*c)
            exit()
