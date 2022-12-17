import copy

dx = [[[0], [-1], [0], [1]], [[-1, 1], [0, 0]], [[0, -1], [-1, 0], [0, 1], [1, 0]],
      [[0, -1, 0], [-1, 0, 1], [0, 1, 0], [1, 0, -1]], [[-1, 0, 1, 0]]]
dy = [[[1], [0], [-1], [0]], [[0, 0], [-1, 1]], [[1, 0], [0, -1], [-1, 0], [0, 1]],
      [[1, 0, -1], [0, -1, 0], [-1, 0, 1], [0, 1, 0]], [[0, -1, 0, 1]]]

N, M = map(int, input().split())
graph = []
cctv = []
wall = []
answer = N * M + 1

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(len(data)):
        if 0 < data[j] <= 5:
            cctv.append([i, j])
        if data[j] == 6:
            wall.append([i, j])


def bfs(current, di_x, di_y, x, y):
    length = len(di_x)
    for k in range(length):
        nx, ny = x + di_x[k], y + di_y[k]
        while True:
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if current[nx][ny] == 6:
                break
            if current[nx][ny] == 0:
                current[nx][ny] = '#'
            nx, ny = nx + di_x[k], ny + di_y[k]


def solve(current):
    result = 0
    for x in range(N):
        for y in range(M):
            if current[x][y] == 0:
                result += 1
    return result


def supervise(cnt, current):
    global answer
    if cnt == len(cctv):
        answer = min(answer, solve(current))
        return
    x, y = cctv[cnt][0], cctv[cnt][1]
    camera = graph[x][y] - 1
    length = len(dx[camera])
    for k in range(length):
        temp = copy.deepcopy(current)
        bfs(current, dx[camera][k], dy[camera][k], x, y)
        supervise(cnt + 1, current)
        current = copy.deepcopy(temp)


supervise(0, graph)
print(answer)
