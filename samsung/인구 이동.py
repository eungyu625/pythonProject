dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * N for _ in range(N)]
answer = 0

while True:
    found = False
    movement = False
    for i in range(N):
        for j in range(N):
            if check[i][j] == 1:
                continue
            country = 1
            population = world[i][j]
            check[i][j] = 1
            queue = [[i, j]]
            temp = [[i, j]]
            while queue:
                x, y = queue.pop(0)
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if check[nx][ny] == 0 and L <= abs(world[nx][ny] - world[x][y]) <= R:
                            check[nx][ny] = 1
                            queue.append([nx, ny])
                            temp.append([nx, ny])
                            country += 1
                            population += world[nx][ny]
            eq = population // country
            if len(temp) > 1:
                found, movement = True, True
            for tx, ty in temp:
                world[tx][ty] = eq
    if not found:
        break
    answer += 1
    if movement:
        for i in range(N):
            for j in range(N):
                check[i][j] = 0

print(answer)
