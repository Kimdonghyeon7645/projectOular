#   23. 두 과잉수의 합으로 나타낼 수 없는 모든 양의 정수의 합은?
abundant_nums, result_nums = list(), list(range(28124))
for n in range(2, 28123):
    if sum((i + n // i) if n // i != i else i for i in range(2, int(n ** (1/2))+1) if n % i == 0) > n-1:
        abundant_nums.append(n)
        for i in abundant_nums:
            if i + n < 28124:
                result_nums[i + n] = 0
print(sum(result_nums))     # 3.2초
# 1~28123 과잉수 합이 아닌 수의 총합을 구하라는 말귀를 오해해서 28123 이상의 두 과잉수 합이 아닌 수를 구하느라 삽질...
