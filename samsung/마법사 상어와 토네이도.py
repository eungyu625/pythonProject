left = [(0, -2, 0.05), (-1, -1, 0.10), (-1, 0, 0.07), (-2, 0, 0.02), (-1, 1, 0.01),
        (1, -1, 0.10), (1, 0, 0.07), (2, 0, 0.02), (1, 1, 0.01), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
up = [(y, x, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
cx, cy = N // 2, N // 2
answer = 0


def solve(time, move, direction):
    global cx, cy, answer
    for _ in range(time):
        cx += dx[direction]
        cy += dy[direction]
        if cy < 0:
            break
        total = 0
        for x, y, rate in move:
            nx = cx + x
            ny = cy + y
            sand = 0
            if rate != 0:
                sand = int(graph[cx][cy] * rate)
                total += sand
            else:
                sand = graph[cx][cy] - total
            if 0 <= nx < N and 0 <= ny < N:
                graph[nx][ny] += sand
            else:
                answer += sand


for i in range(1, N + 1):
    if i % 2:
        solve(i, left, 0)
        solve(i, down, 1)
    else:
        solve(i, right, 2)
        solve(i, up, 3)

print(answer)
