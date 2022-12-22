dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
graph = []
virus = []
answer = int(1e9)

for a in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for b in range(len(data)):
        if data[b] == 2:
            virus.append([a, b])


def solve(temp):
    current = [[-1] * N for _ in range(N)]
    queue = []
    for tx, ty in temp:
        current[tx][ty] = 0
        queue.append([tx, ty])

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] != 1 and current[nx][ny] == -1:
                    current[nx][ny] = current[x][y] + 1
                    queue.append([nx, ny])

    result = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                if current[i][j] == -1:
                    return int(1e9)
                result = max(result, current[i][j])

    return result


def choose(cnt, start, temp):
    global answer
    if cnt == M:
        answer = min(answer, solve(temp))
        return

    for i in range(start, len(virus)):
        temp.append(virus[i])
        choose(cnt + 1, i + 1, temp)
        temp.pop()


choose(0, 0, [])

print(answer if answer != int(1e9) else -1)
