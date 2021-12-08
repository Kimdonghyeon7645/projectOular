#   21. 10000 이하 모든 친화수(우애수)의 합은?
divisor_list = [0] + [1 for _ in range(9999)]
cnt = 0
for num in range(2, 10001):
    for i in range(2, int(num ** (1/2))+1):
        if num % i == 0:
            divisor_list[num-1] += (i + num // i) if num // i != i else i
for a in range(2, 10001):
    b = divisor_list[a-1]
    if 10000 >= b != a and a == divisor_list[b - 1]:
        cnt += a + b
        divisor_list[b - 1] = 0
#   막혔던 포인트 : '서로 다른 두 정수 a, b' 를 간과했다.. / d(a) == a 인 수는 완전수라 하여, 친화수가 아니다!
print(cnt)
