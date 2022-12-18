dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

r, c, t = map(int, input().split())
graph = []
cleaner = []

for a in range(r):
    data = list(map(int, input().split()))
    graph.append(data)
    for b in range(len(data)):
        if data[b] == -1:
            cleaner.append([a, b])


def diffusion():
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                continue
            count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                    temp[nx][ny] += graph[i][j] // 5
                    count += 1
            graph[i][j] -= (graph[i][j] // 5) * count
    for i in range(r):
        for j in range(c):
            graph[i][j] += temp[i][j]


def upper_clean():
    ux = [0, -1, 0, 1]
    uy = [1, 0, -1, 0]

    x, y = cleaner[0][0], cleaner[0][1] + 1
    res = graph[x][y]
    graph[x][y] = 0
    di = 0
    while True:
        nx, ny = x + ux[di], y + uy[di]
        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            di += 1
            continue
        if graph[nx][ny] == -1:
            break
        res, graph[nx][ny] = graph[nx][ny], res
        x, y = nx, ny


def lower_clean():
    lx = [0, 1, 0, -1]
    ly = [1, 0, -1, 0]

    x, y = cleaner[1][0], cleaner[1][1] + 1
    res = graph[x][y]
    graph[x][y] = 0
    di = 0
    while True:
        nx, ny = x + lx[di], y + ly[di]
        if 0 > nx or nx >= r or 0 > ny or ny >= c:
            di += 1
            continue
        if graph[nx][ny] == -1:
            break
        res, graph[nx][ny] = graph[nx][ny], res
        x, y = nx, ny


for _ in range(t):
    diffusion()
    upper_clean()
    lower_clean()

answer = 0
for i in range(r):
    for j in range(c):
        answer += graph[i][j]

print(answer + 2)
