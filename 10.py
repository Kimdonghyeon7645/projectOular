#   10. 이백만 이하 소수의 합
sum_so_su = 0
for su in range(2, 2000000):
    is_so_su = True
    for i in range(2, int(su**(1/2))+1):
        if su % i == 0:
            is_so_su = False
            break
    if is_so_su:
        sum_so_su += su
print(sum_so_su)
