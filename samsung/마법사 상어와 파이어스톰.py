dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, Q = map(int, input().split())
n = pow(2, N)
graph = [list(map(int, input().split())) for _ in range(n)]
magics = list(map(int, input().split()))


def picture():
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()
    print()


def melt():
    check = [[True] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            res = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0:
                        res += 1
            if res < 3:
                check[i][j] = False
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                graph[i][j] -= 1


def rotate(x, y, interval):
    result = [[0] * interval for _ in range(interval)]
    for i in range(interval):
        for j in range(interval):
            result[j][interval - i - 1] = graph[x + i][y + j]
    for i in range(interval):
        for j in range(interval):
            graph[x + i][y + j] = result[i][j]


def solve(interval):
    for i in range(0, n, interval):
        for j in range(0, n, interval):
            rotate(i, j, interval)
    melt()


for magic in magics:
    solve(pow(2, magic))

answer = 0
lump = 0
visited = [[False] * n for _ in range(n)]
for a in range(n):
    for b in range(n):
        answer += graph[a][b]
        if graph[a][b] == 0:
            continue
        if visited[a][b]:
            continue
        queue = [[a, b]]
        result = 1
        visited[a][b] = True
        while queue:
            x, y = queue.pop(0)
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] != 0 and not visited[nx][ny]:
                        result += 1
                        visited[nx][ny] = True
                        queue.append([nx, ny])
        lump = max(lump, result)

print(answer)
print(lump)
