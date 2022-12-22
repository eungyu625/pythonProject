dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
graph = []
sx, sy = 0, 0
shark_size = 2
shark_num = 0
time = 0
prey = []

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(N):
        if data[j] == 9:
            sx, sy = i, j
        elif data[j] != 0:
            prey.append([i, j])

while prey:
    current = []
    for x, y in prey:
        if graph[x][y] < shark_size:
            current.append([x, y])
    if not current:
        break
    temp = [[-1] * N for _ in range(N)]
    temp[sx][sy] = 0
    queue = [[sx, sy]]
    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] > shark_size:
                    continue
                if temp[nx][ny] == -1:
                    temp[nx][ny] = temp[x][y] + 1
                    queue.append([nx, ny])

    eat = []
    for x, y in current:
        if temp[x][y] > 0:
            eat.append([x, y, temp[x][y]])
    if not eat:
        break
    eat.sort(key=lambda l: (l[-1], l[0], l[1]))
    px, py, p_dist = eat[0]
    prey.remove([px, py])
    graph[sx][sy] = 0
    graph[px][py] = 9
    sx, sy = px, py
    time += p_dist
    shark_num += 1
    if shark_num == shark_size:
        shark_size += 1
        shark_num = 0

print(time)
