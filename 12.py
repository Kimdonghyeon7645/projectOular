#   12. 500개 이상의 약수를 갖는 가장 작은 삼각수는?
sam_gag_su = add_num = 1
while sam_gag_su < 100000000:
    divisor_cnt = 0
    root_su = sam_gag_su**(1/2)
    add_num += 1
    sam_gag_su += add_num
    for i in range(1, int(root_su)):
        if sam_gag_su % i == 0:
            divisor_cnt += 2
    if sam_gag_su % root_su == 0:
        divisor_cnt += 1
    if divisor_cnt >= 500:
        print(sam_gag_su)
        break
