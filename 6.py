#   6. 1부터 100까지 "제곱의 합"과 "합의 제곱"의 차는?
print(sum(i for i in range(1, 101))**2 - sum(i**2 for i in range(1, 101)))
