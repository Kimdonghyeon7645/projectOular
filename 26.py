#   26. 1000 이하의 d 중에서 1/d 이 가장 긴 순환마디를 갖는 수는?
cycle_list = list()
for num in range(2, 1001):
    remainder_list = [1]
    for i in range(1000):   # 소수점 아래로 1000개 까지만 검사
        if remainder_list[-1] * 10 < num:
            remainder_list.append(remainder_list[-1] * 10)
        else:
            remainder = remainder_list[-1] * 10 % num
            if remainder == 0:
                cycle_list.append(0)
                break
            elif remainder in remainder_list:
                cycle_list.append(len(remainder_list) - remainder_list.index(remainder))
                break
            else:
                remainder_list.append(remainder)
print(cycle_list.index(max(cycle_list))+2)      # 평균 0.23초 소요
