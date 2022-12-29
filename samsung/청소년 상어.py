dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[] for _ in range(4)]
answer = 0

for a in range(4):
    data = list(map(int, input().split()))
    fishes =[]
    for b in range(4):
        ai, bi = data[2 * b], data[2 * b + 1] - 1
        fishes.append([ai, bi])
    graph[a] = fishes


def deepcopy(mutable):
    if type(mutable) != list:
        return mutable
    now = []
    for item in mutable:
        now.append(deepcopy(item))
    return now


def solve(sx, sy, result, current):
    global answer
    result += current[sx][sy][0]
    answer = max(result, answer)
    current[sx][sy][0] = 0

    for fish in range(1, 17):
        fx, fy = -1, -1
        for i in range(4):
            for j in range(4):
                if current[i][j][0] == fish:
                    fx, fy = i, j
                    break
        if fx == -1 and fy == -1:
            continue

        di = current[fx][fy][1]
        for _ in range(8):
            nx, ny = fx + dx[di], fy + dy[di]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if nx != sx or ny != sy:
                    current[fx][fy][1] = di
                    current[fx][fy], current[nx][ny] = current[nx][ny], current[fx][fy]
                    break
            di = (di + 1) % 8
    di = current[sx][sy][1]
    for k in range(1, 4):
        nx, ny = sx + dx[di] * k, sy + dy[di] * k
        if 0 <= nx < 4 and 0 <= ny < 4:
            if current[nx][ny][0] != 0:
                solve(nx, ny, result, deepcopy(current))


solve(0, 0, 0, graph)
print(answer)
