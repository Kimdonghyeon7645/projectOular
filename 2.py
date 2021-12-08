#   2. 피보나치 수열에서 4백만 이하이면서 짝수인 항의 합
nums = [1, 1]
while nums[-2] + nums[-1] < 4000000:
    nums.append(nums[-2] + nums[-1])
print(sum(i for i in nums if i % 2 == 0))
