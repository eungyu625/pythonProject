dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[[] for _ in range(4)] for _ in range(4)]
answer = 0

for a in range(4):
    data = list(map(int, input().split()))
    temp = []
    for b in range(len(data)):
        ai, bi = data[2 * b], data[2 * b - 1] + 1
        temp.append([ai, bi])
    graph[a] = temp


def deepcopy(mutable):
    if type(mutable) != list:
        return mutable
    now = []
    for item in mutable:
        now.append(deepcopy(item))
    return now


def move(sx, sy, result, current):
    global answer
    result += current[sx][sy][0]
    answer = max(result, answer)
    current[sx][sy][0] = 0

    for fish in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if current[x][y][0] == fish:
                    fx, fy = x, y
                    break
        if fx == -1 and fy == -1:
            continue
        di = current[fx][fy][1]
        for _ in range(8):
            nx, ny = fx + dx[di], fy + dy[di]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if nx != sx or ny != sy:
                    current[nx][ny][1] = di
                    current[fx][fy], current[nx][ny] = current[nx][ny], current[fx][fy]
                    break
            di = (di + 1) % 8

    di = current[sx][sy][1]
    for k in range(1, 4):
        nx, ny = sx + dx[di] * k, sy + dy[di] * k
        if 0 <= nx < 4 and 0 <= ny < 4:
            if current[nx][ny][0] != 0:
                move(nx, ny, result, deepcopy(current))


move(0, 0, 0, graph)
print(answer)
