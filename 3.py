#   3. 가장 큰 소인수 구하기
su = 600851475143
small_su = 2
so_in_su = [1]
while small_su < su:
    if su % small_su == 0:
        so_in_su.append(small_su)
        su //= small_su
    else:
        small_su += 1
so_in_su.append(su)
print(so_in_su[-1])
