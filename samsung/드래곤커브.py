dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

N = int(input())
graph = [[0] * 110 for _ in range(110)]
dragon = []

for _ in range(N):
    dragon.append(list(map(int, input().split())))

for x, y, d, g in dragon:
    graph[y][x] = 1
    curve = [d]
    for _ in range(g):
        length = len(curve)
        for i in range(length - 1, -1, -1):
            nd = curve[i]
            curve.append((nd + 1) % 4)
    nx, ny = x, y
    for direction in curve:
        nx += dx[direction]
        ny += dy[direction]
        graph[ny][nx] = 1

result = 0
for i in range(101):
    for j in range(101):
        if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
            result += 1

print(result)
