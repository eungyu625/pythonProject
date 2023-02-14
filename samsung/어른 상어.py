dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
directions = list(map(int, input().split()))
priorities = []

for _ in range(M):
    temp = []
    for _ in range(4):
        data = list(map(int, input().split()))
        temp.append(data)
    priorities.append(temp)

smell = [[[0, 0]] * N for _ in range(N)]


def smelling():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            if arr[i][j] != 0:
                smell[i][j] = [arr[i][j], k]


def solve():
    new_data = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                continue
            direction = directions[arr[i][j] - 1]
            found = False
            for index in priorities[arr[i][j] - 1][direction - 1]:
                nx, ny = i + dx[index - 1], j + dy[index - 1]
                if 0 <= nx < N and 0 <= ny < N:
                    if smell[nx][ny][1] == 0:
                        directions[arr[i][j] - 1] = index
                        found = True
                        if new_data[nx][ny] == 0:
                            new_data[nx][ny] = arr[i][j]
                        else:
                            new_data[nx][ny] = min(new_data[nx][ny], arr[i][j])
                        break
            if found:
                continue

            for index in priorities[arr[i][j] - 1][direction - 1]:
                nx, ny = i + dx[index - 1], j + dy[index - 1]
                if 0 <= nx < N and 0 <= ny < N:
                    if smell[nx][ny][0] == arr[i][j]:
                        directions[arr[i][j] - 1] = index
                        new_data[nx][ny] = arr[i][j]
                        break
    return new_data


answer = 0
while True:
    smelling()
    arr = solve()
    check = True
    for a in range(N):
        for b in range(N):
            if arr[a][b] > 1:
                check = False
                break
    if check:
        print(answer)
        break
    answer += 1
    if answer >= 1000:
        print(-1)
        break
