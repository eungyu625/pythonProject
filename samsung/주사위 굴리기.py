dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dice = [0, 0, 0, 0, 0, 0, 0]
# 최초 : 1, 2, 3, 5, 4, 6
# 동쪽 : 4, 2, 1, 5, 6, 3
# 서쪽 : 3, 2, 6, 5, 1, 4
# 북쪽 : 5, 1, 3, 6, 4, 2
# 남쪽 : 2, 6, 3, 1, 4, 5

moves = list(map(int, input().split()))

for move in moves:
    nx, ny = x + dx[move - 1], y + dy[move - 1]
    if nx >= N or nx < 0 or ny >= M or ny < 0:
        continue
    if move == 1:
        dice[1], dice[2], dice[3], dice[5], dice[4], dice[6] = dice[4], dice[2], dice[1], dice[5], dice[6], dice[3]
    elif move == 2:
        dice[1], dice[2], dice[3], dice[5], dice[4], dice[6] = dice[3], dice[2], dice[6], dice[5], dice[1], dice[4]
    elif move == 3:
        dice[1], dice[2], dice[3], dice[5], dice[4], dice[6] = dice[5], dice[1], dice[3], dice[6], dice[4], dice[2]
    elif move == 4:
        dice[1], dice[2], dice[3], dice[5], dice[4], dice[6] = dice[2], dice[6], dice[3], dice[1], dice[4], dice[5]
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[6]
    else:
        dice[6] = graph[nx][ny]
        graph[nx][ny] = 0
    print(dice[1])
    x, y = nx, ny
