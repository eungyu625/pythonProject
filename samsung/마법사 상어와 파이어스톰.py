N, Q = map(int, input().split())
n = pow(2, N)
graph = [list(map(int, input().split())) for _ in range(n)]
magics = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def melt():
    check = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            res = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] > 0:
                        res += 1
            check[i][j] = res
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                continue
            if check[i][j] < 3:
                graph[i][j] -= 1


def rotate(x, y, length):
    result = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            result[j][length - i - 1] = graph[x + i][y + j]
    for i in range(length):
        for j in range(length):
            graph[x + i][y + j] = result[i][j]


def firestorm(index):
    for i in range(0, n, index):
        for j in range(0, n, index):
            rotate(i, j, index)
    melt()


def solve():
    check = [[False] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                continue
            if graph[i][j] == 0:
                continue
            middle = 1
            check[i][j] = True
            queue = [[i, j]]
            while queue:
                x, y = queue.pop(0)
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if not check[nx][ny] and graph[nx][ny] > 0:
                            check[nx][ny] = True
                            middle += 1
                            queue.append([nx, ny])
            result = max(result, middle)
    print(result)


for magic in magics:
    firestorm(pow(2, magic))

answer = 0
for a in range(n):
    for b in range(n):
        answer += graph[a][b]

print(answer)
solve()