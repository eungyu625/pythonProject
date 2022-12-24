N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = int (1e9)

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]


def solve(check):
    global answer
    first, second, third, forth, fifth = 0, 0, 0, 0, 0
    for i in range(N):
        for j in range(N):
            if check[i][j] == 1:
                first += graph[i][j]
            elif check[i][j] == 2:
                second += graph[i][j]
            elif check[i][j] == 3:
                third += graph[i][j]
            elif check[i][j] == 4:
                forth += graph[i][j]
            else:
                fifth += graph[i][j]
    max_num = max(first, second, third, forth, fifth)
    min_num = min(first, second, third, forth, fifth)
    answer = min(answer, max_num - min_num)


def make_first(x, y, dist_1, check):
    for i in range(x):
        for j in range(y + dist_1 + 1):
            if check[i][j] == 5:
                break
            check[i][j] = 1


def make_second(x, dist_1, dist_2, check):
    for i in range(x - dist_1 + dist_2 + 1):
        for j in range(N - 1, -1, -1):
            if check[i][j] != 0:
                break
            check[i][j] = 2


def make_third(x, y, dist_2, check):
    for i in range(x, N):
        for j in range(y + dist_2):
            if check[i][j] == 5:
                break
            check[i][j] = 3


def make_forth(x, dist_1, dist_2, check):
    for i in range(x - dist_1 + dist_2 + 1, N):
        for j in range(N - 1, -1, -1):
            if check[i][j] != 0:
                break
            check[i][j] = 4


def make_fifth(x, y, dist_1, dist_2, check):
    di = 0
    sx, sy = x, y
    check[sx][sy] = 5
    while True:
        nx, ny = sx + dx[di], sy + dy[di]
        if nx == x and ny == y:
            break
        check[nx][ny] = 5
        if nx == x - dist_1 and ny == y + dist_1:
            di = 1
        if nx == x - dist_1 + dist_2 and ny == y + dist_1 + dist_2:
            di = 2
        if nx == x + dist_2 and ny == y + dist_2:
            di = 3
        sx, sy = nx, ny


def make_ring(x, y, dist_1, dist_2):
    check = [[0] * N for _ in range(N)]
    check[x][y] = 5
    make_fifth(x, y, dist_1, dist_2, check)
    make_first(x, y, dist_1, check)
    make_second(x, dist_1, dist_2, check)
    make_third(x, y, dist_2, check)
    make_forth(x, dist_1, dist_2, check)
    solve(check)


def gerrymandering():
    for i in range(1, N // 2 + 1):
        for j in range(1, N // 2 + 1):
            for x in range(i, N - j):
                for y in range(N - i - j):
                    make_ring(x, y, i, j)


gerrymandering()
print(answer)
