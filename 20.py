#   20. 100! 의 자릿수를 모두 더하면?
print(sum(map(int, str(eval("*".join(map(str, range(1, 100))))))))
