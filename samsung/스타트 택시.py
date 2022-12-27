dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
taxi = [tx - 1, ty - 1]

start, end = [], []
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    start.append([sx - 1, sy - 1])
    end.append([ex - 1, ey - 1])


def go_to_passenger():
    dist = [[-1] * N for _ in range(N)]
    dist[taxi[0]][taxi[1]] = 0
    queue = [taxi]
    min_dist = int(1e9)
    candidate = []
    while queue:
        x, y = queue.pop(0)
        if dist[x][y] > min_dist:
            break
        if [x, y] in start:
            candidate.append([x, y])
            min_dist = dist[x][y]
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
    if not candidate:
        return -1, -1, -1
    candidate.sort()
    return dist[candidate[0][0]][candidate[0][1]], candidate[0][0], candidate[0][1]


def go_to_destination(end_x, end_y):
    dist = [[-1] * N for _ in range(N)]
    dist[taxi[0]][taxi[1]] = 0
    queue = [taxi]
    while queue:
        x, y = queue.pop(0)
        if x == end_x and y == end_y:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
    return dist[end_x][end_y]


for _ in range(M):
    start_di, sx, sy = go_to_passenger()
    if start_di == -1 or fuel < start_di:
        fuel = -1
        break
    fuel -= start_di
    taxi = [sx, sy]
    index = start.index([sx, sy])
    start[index] = [-1, -1]
    ex, ey = end[index]
    end_di = go_to_destination(ex, ey)
    if end_di == -1 or fuel < end_di:
        fuel = -1
        break
    fuel += end_di
    taxi = [ex, ey]

print(fuel)