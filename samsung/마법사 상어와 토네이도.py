left = [(0, -2, 0.05), (-1, -1, 0.10), (-1, 0, 0.07), (-2, 0, 0.02), (-1, 1, 0.01), (1, -1, 0.10), (1, 0, 0.07),
        (2, 0, 0.02), (1, 1, 0.01), (0, -1, 0)]
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
        for x, y, z in move:
            nx, ny = cx + x, cy + y
            sand = 0
            if z == 0:
                sand = graph[cx][cy] - total
            else:
                sand = int(graph[cx][cy] * z)
                total += sand
            if 0 <= nx < N and 0 <= ny < N:
                graph[nx][ny] += sand
            else:
                answer += sand


for i in range(1, N + 1):
    if i % 2 == 1:
        solve(i, left, 0)
        solve(i, down, 1)
    else:
        solve(i, right, 2)
        solve(i, right, 3)

print(answer)