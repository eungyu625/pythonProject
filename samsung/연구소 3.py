dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

N, M = map(int, input().split())
arr = []
virus = []
answer = int(1e9)

for d in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for v in range(len(data)):
        if data[v] == 2:
            virus.append([d, v])


def check(current):
    for i in range(N):
        for j in range(N):
            if current[i][j] == -1 and arr[i][j] == 0:
                return False
    return True


def solve(current):
    global answer
    temp = [[-1] * N for _ in range(N)]
    queue = []
    for i, j in current:
        temp[i][j] = 0
        queue.append([i, j])
    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] != 1 and temp[nx][ny] == -1:
                    temp[nx][ny] = temp[x][y] + 1
                    queue.append([nx, ny])
    if not check(temp):
        return
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2 and temp[i][j] != 0:
                temp[i][j] = -2
    result = 0
    for i in range(N):
        for j in range(N):
            result = max(result, temp[i][j])
    answer = min(answer, result)
    return


def choose(index, start, temp):
    if index == M:
        solve(temp)
        return
    for idx in range(start, len(virus)):
        temp.append(virus[idx])
        choose(index + 1, idx + 1, temp)
        temp.pop()


choose(0, 0, [])
print(answer) if answer < int(1e9) else print(-1)
