dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
cleaner = []

for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            cleaner.append([i, j])


def diffusion():
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 0 or arr[i][j] == -1:
                continue
            now = arr[i][j]
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    if arr[nx][ny] == -1:
                        continue
                    arr[i][j] -= now // 5
                    temp[nx][ny] += now // 5

    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]


def upper_cleaner():
    cx, cy = cleaner[0][0], cleaner[0][1] + 1
    ux = [0, -1, 0, 1]
    uy = [1, 0, -1, 0]
    ud = 0
    temp = arr[cx][cy]
    arr[cx][cy] = 0
    while True:
        nx, ny = cx + ux[ud], cy + uy[ud]
        if [nx, ny] == cleaner[0]:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            ud += 1
            continue
        temp, arr[nx][ny] = arr[nx][ny], temp
        cx, cy = nx, ny


def lower_cleaner():
    cx, cy = cleaner[1][0], cleaner[1][1] + 1
    lx = [0, 1, 0, -1]
    ly = [1, 0, -1, 0]
    ld = 0
    temp = arr[cx][cy]
    arr[cx][cy] = 0
    while True:
        nx, ny = cx + lx[ld], cy + ly[ld]
        if [nx, ny] == cleaner[1]:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            ld += 1
            continue
        temp, arr[nx][ny] = arr[nx][ny], temp
        cx, cy = nx, ny


for _ in range(T):
    diffusion()
    upper_cleaner()
    lower_cleaner()

answer = 0
for i in range(R):
    for j in range(C):
        answer += arr[i][j]

print(answer + 2)
