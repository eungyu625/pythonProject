n, a, b = 8, 4, 7

answer = 0
while True:
    if a == b:
        break
    a = (a + 1) // 2
    b = (b + 1) // 2
    answer += 1

print(answer)
