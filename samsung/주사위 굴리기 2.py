dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dice = [0, 1, 2, 3, 4, 5, 6]
# 동쪽 : 4, 2, 1, 6, 5, 3
# 남쪽 : 2, 6, 3, 4, 1, 5
# 서쪽 : 3, 2, 6, 1, 5, 4
# 북쪽 : 5, 1, 3, 4, 6, 2

sx, sy, di = 0, 0, 0
answer = 0


def roll_dice(move):
    if move == 0:
        dice[1], dice[2], dice[3], dice[5], dice[4], dice[6] = dice[4], dice[2], dice[1], dice[5], dice[6], dice[3]
    elif move == 1:
        dice[1], dice[2], dice[3], dice[5], dice[4], dice[6] = dice[2], dice[6], dice[3], dice[1], dice[4], dice[5]
    elif move == 2:
        dice[1], dice[2], dice[3], dice[5], dice[4], dice[6] = dice[3], dice[2], dice[6], dice[5], dice[1], dice[4]
    elif move == 3:
        dice[1], dice[2], dice[3], dice[5], dice[4], dice[6] = dice[5], dice[1], dice[3], dice[6], dice[4], dice[2]


for _ in range(K):
    nx, ny = sx + dx[di], sy + dy[di]
    if 0 > nx or nx >= N or 0 > ny or ny >= M:
        di = (di + 2) % 4
        nx, ny = sx + dx[di], sy + dy[di]
    roll_dice(di)
    if dice[6] > graph[nx][ny]:
        di = (di + 1) % 4
    elif dice[6] < graph[nx][ny]:
        di = (di - 1) % 4
    b = graph[nx][ny]
    queue = [[nx, ny]]
    check = [[False] * M for _ in range(N)]
    check[nx][ny] = True
    c = 1
    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            ax, ay = x + dx[k], y + dy[k]
            if 0 <= ax < N and 0 <= ay < M:
                if graph[ax][ay] == b and not check[ax][ay]:
                    check[ax][ay] = True
                    c += 1
                    queue.append([ax, ay])
    answer += b * c
    sx, sy = nx, ny

print(answer)
