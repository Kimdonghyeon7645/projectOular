#   5. 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수
so_su = (2, 3, 5, 7, 11, 13, 17, 19)
cnt_so_su = dict().fromkeys(so_su, 0)


def get_so_su(num: int) -> list:
    result = []
    while num > 1:
        for su in so_su:
            if num % su == 0:
                num //= su
                result.append(su)
                break
    return result


for i in range(1, 20):
    li = get_so_su(i)
    for su in so_su:
        if cnt_so_su[su] < li.count(su):
            cnt_so_su[su] = li.count(su)
print(eval("*".join([str(item[0]**item[1]) for item in cnt_so_su.items()])))
