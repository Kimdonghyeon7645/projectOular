#   7. 10001번째의 소수
so_su_list = []
su = 1
while len(so_su_list) < 10001:
    su += 1
    is_so_su = True
    for i in range(2, int(su**(1/2))+1):
        if su % i == 0:
            is_so_su = False
            break
    if is_so_su:
        so_su_list.append(su)
print(so_su_list[-1])
