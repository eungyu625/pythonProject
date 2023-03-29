dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tx, ty = map(int, input().split())
taxi = [tx - 1, ty - 1]
start, end = [], []
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    start.append([sx - 1, sy - 1])
    end.append([ex - 1, ey - 1])


def take_on_passenger():
    dist = [[-1] * N for _ in range(N)]
    candidate = []
    dist[taxi[0]][taxi[1]] = 0
    queue = [[taxi[0], taxi[1]]]
    min_dist = int(1e9)
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
                if dist[nx][ny] == -1 and arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
    if not candidate:
        return -1, -1, -1
    candidate.sort()
    return candidate[0][0], candidate[0][1], dist[candidate[0][0]][candidate[0][1]]


def go_to_destination(end_x, end_y):
    dist = [[-1] * N for _ in range(N)]
    dist[taxi[0]][taxi[1]] = 0
    queue = [[taxi[0], taxi[1]]]
    while queue:
        x, y = queue.pop(0)
        if x == end_x and y == end_y:
            break
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] == -1 and arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
    return dist[end_x][end_y]


for _ in range(M):
    sx, sy, sdist = take_on_passenger()
    if sdist > fuel or sdist == -1:
        fuel = -1
        break
    fuel -= sdist
    taxi = [sx, sy]
    index = start.index([sx, sy])
    start[index] = [-1, -1]
    edist = go_to_destination(end[index][0], end[index][1])
    if edist > fuel or edist == -1:
        fuel = -1
        break
    taxi = [end[index][0], end[index][1]]
    fuel += edist

print(fuel)
