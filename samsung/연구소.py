dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())
arr = []
virus = []
answer = 0

for a in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for b in range(len(data)):
        if data[b] == 2:
            virus.append([a, b])


def deepcopy(mutable):
    if type(mutable) != list:
        return mutable
    now = []
    for item in mutable:
        now.append(deepcopy(item))
    return now


def solve(temp):
    global answer
    current = deepcopy(temp)
    queue = []
    for x, y in virus:
        queue.append([x, y])
    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if current[nx][ny] == 0:
                    current[nx][ny] = 2
                    queue.append([nx, ny])
    result = 0
    for i in range(N):
        for j in range(M):
            if current[i][j] == 0:
                result += 1
    answer = max(answer, result)


def new_wall(index, temp):
    if index == 3:
        solve(temp)
        return
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                temp[i][j] = 1
                new_wall(index + 1, temp)
                temp[i][j] = 0


new_wall(0, arr)
print(answer)
