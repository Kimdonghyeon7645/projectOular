#   15. 20×20 격자의 좌상단에서 우하단으로 가는 경로의 수
# 2학년 때 확통 배운거 활용 : https://j1w2k3.tistory.com/712
print(eval(f"({'*'.join(map(str, range(1, 41)))})//({'*'.join(map(str, range(1, 21)))})**2"))
