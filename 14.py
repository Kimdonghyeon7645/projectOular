#   14. 백만 이하로 시작하는 우박수 중 가장 긴 과정을 거치는 것은?
#   직접 하나씩 확인 (Brute Force)     == 35초
# max_num, max_cnt = 1, 1
# for num in range(1, 1000001):
#     i = num
#     cnt = 0
#     while i != 1:
#         i = i/2 if i % 2 == 0 else 3*i + 1
#         cnt += 1
#     max_num, max_cnt = (max_num, max_cnt) if max_cnt > cnt else (num, cnt)
# print(max_num)

#   메모이제이션 + list 자료형 (인덱스) == 1.5~2.0초
hailstone_su_list = list()
for num in range(1, 1000001):
    cnt, i = 0, num
    while i != 1:
        if i+1 < num:
            cnt += hailstone_su_list[i-1]
            break
        else:
            i = i//2 if i % 2 == 0 else 3*i + 1
            cnt += 1
    hailstone_su_list.append(cnt)
print(hailstone_su_list.index(max(hailstone_su_list))+1)

#   메모이제이션 + dictionary 자료형 (해시 테이블) == 2.4~3.8초
hailstone_su_dict = dict()
for num in range(1, 1000001):
    cnt, i = 0, num
    while i != 1:
        if hailstone_su_dict.get(i):
            cnt += hailstone_su_dict[i]
            break
        else:
            i = i//2 if i % 2 == 0 else 3*i + 1
            cnt += 1
    hailstone_su_dict[num] = cnt
print(sorted(hailstone_su_dict.items(), key=lambda x: -x[1])[0])
