dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M, fuel = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
taxi = [tx - 1, ty - 1]
start, end = [], []

for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    start.append([sx, sy])
    end.append([ex, ey])


def move_to_passenger():
    dist = [[-1] * N for _ in range(N)]
    queue = [taxi]
    dist[taxi[0]][taxi[1]] = 0
    min_dist = int(1e9)
    candidate = []
    while queue:
        x, y = queue.pop(0)
        if dist[x][y] > min_dist:
            break
        if [x, y] in candidate:
            candidate.append([x, y])
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
    if not candidate:
        return -1, -1, -1
    candidate.sort()
    return candidate[0][0], candidate[0][1], dist[candidate[0][0]][candidate[0][1]]


def move_to_destination(end_x, end_y):
    dist = [[-1] * N for _ in range(N)]
    queue = [taxi]
    dist[taxi[0]][taxi[1]] = 0
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
    sx, sy, start_dist = move_to_passenger()
    if start_dist == -1 or start_dist > fuel:
        fuel = -1
        break
    fuel -= start_dist
    taxi = [sx, sy]
    index = start.index([sx, sy])
    start[index] = [-1, -1]
    ex, ey = end[index]
    end_dist = move_to_destination(ex, ey)
    if end_dist == -1 or end_dist > fuel:
        fuel = -1
        break
    fuel += end_dist
    taxi = [ex, ey]

print(fuel)
