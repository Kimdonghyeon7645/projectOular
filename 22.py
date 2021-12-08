#   22. 영문 이름 점수 합계 구하기
with open("names.txt") as f:
    print(sum((i+1) * sum(ord(ch)-64 for ch in name)
              for i, name in enumerate(sorted(f.read().replace('"', '').split(",")))))
