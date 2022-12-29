def deepcopy(mutable):
    if type(mutable) != list:
        return mutable
    now = []
    for item in mutable:
        now.append(deepcopy(item))
    return now


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
d = [1, -1]
N, M, T = map(int, input().split())

graph = [[] for _ in range(N + 1)]
rotation = []

for a in range(1, N + 1):
    graph[a] = list(map(int, input().split()))

for _ in range(T):
    rotation.append(list(map(int, input().split())))


def average_number():
    avg = 0
    num = 0
    for i in range(1, N + 1):
        for j in range(M):
            if graph[i][j] != 'X':
                avg += graph[i][j]
                num += 1
    if num == 0:
        return
    avg /= num
    for i in range(1, N + 1):
        for j in range(M):
            if graph[i][j] == 'X':
                continue
            if graph[i][j] > avg:
                graph[i][j] -= 1
            elif graph[i][j] < avg:
                graph[i][j] += 1


def del_number():
    check = [[False] * M for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(M):
            for k in range(4):
                nx, ny = i + dx[k], (j + dy[k]) % M
                if 1 <= nx <= N:
                    if graph[i][j] == 'X' or graph[nx][ny] == 'X':
                        continue
                    if graph[i][j] == graph[nx][ny]:
                        check[i][j] = True
                        check[nx][ny] = True
    adjoin = False
    for i in range(1, N + 1):
        for j in range(M):
            if check[i][j]:
                graph[i][j] = 'X'
                adjoin = True
    if not adjoin:
        average_number()


def solve():
    for xi, di, ki in rotation:
        for i in range(xi, N + 1, xi):
            res = deepcopy(graph[i])
            for j in range(M):
                graph[i][(j + d[di] * ki) % M] = res[j]
        del_number()


solve()
answer = 0
for a in range(1, N + 1):
    for b in range(M):
        if graph[a][b] != 'X':
            answer += graph[a][b]
print(answer)
