#   25. 피보나치 수열에서 처음으로 1000자리가 되는 항은 몇 번째?
f_list = [1, 1]
while f_list[-1] < 10**999:
    f_list.append(f_list[-2] + f_list[-1])
print(len(str(f_list[-1])))
print(f_list[-1], len(f_list))
