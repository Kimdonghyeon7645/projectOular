#   24. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 1,000,000번째 사전식 순열은?
cnt = 1000000 - 1
su = [i for i in range(10)]
result = [0 for i in range(10)]
while cnt > 0:
    n = 1
    idx = 1
    for i in range(2, 11):
        if n*i <= cnt:
            n *= i
        else:
            idx = i-1
            break
    for j in range(2, 11):
        if n*j > cnt:
            n *= (j-1)
            result[9-idx] = su.pop(j-1)
            break
    cnt -= n
print("".join(map(str, result)))
