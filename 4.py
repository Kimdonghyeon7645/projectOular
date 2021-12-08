#   4. 세자리 수를 곱해 만들 수 있는 가장 큰 대칭수
print(sorted([i*j for i in range(999, 2, -1) for j in range(999, 2, -1) if str(i*j) == str(i*j)[::-1]])[-1])
