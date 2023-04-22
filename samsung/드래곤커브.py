dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N = int(input())
arr = [[0] * 110 for _ in range(110)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr[y][x] = 1
    curves = [d]
    for now in range(1, g + 1):
        length = len(curves)
        new_curve = []
        for a in range(length):
            new_curve.append((curves[a] + 1) % 4)
        new_curve.reverse()
        curves = curves + new_curve
    for curve in curves:
        x, y = x + dx[curve], y + dy[curve]
        arr[y][x] = 1

answer = 0
for i in range(105):
    for j in range(105):
        if arr[i][j] == 1 and arr[i + 1][j] == 1 and arr[i][j + 1] == 1 and arr[i + 1][j + 1] == 1:
            answer += 1
print(answer)
