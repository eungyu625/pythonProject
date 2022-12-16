dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
graph = []
virus = []

for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(len(data)):
        if data[j] == 2:
            virus.append([i, j])

ans = -1


def default(temp):
    curr = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            curr[x][y] = temp[x][y]
    return curr


def solve(current):
    result = default(current)
    queue = []
    for v in virus:
        queue.append(v)

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if result[nx][ny] == 0:
                    result[nx][ny] = 2
                    queue.append([nx, ny])
    res = 0
    for x in range(n):
        for y in range(m):
            if result[x][y] == 0:
                res += 1

    return res


def build(cnt, current):
    global ans
    if cnt == 3:
        ans = max(ans, solve(current))
        return

    for x in range(n):
        for y in range(m):
            if current[x][y] == 0:
                current[x][y] = 1
                build(cnt + 1, current)
                current[x][y] = 0


build(0, graph)
print(ans)
