dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
arr = []
shark = []
size = 2
number = 0

for a in range(N):
    data = list(map(int, input().split()))
    arr.append(data)
    for b in range(len(data)):
        if data[b] == 9:
            shark = [a, b]

answer = 0
while True:
    if number == size:
        number = 0
        size += 1
    temp = [[-1] * N for _ in range(N)]
    temp[shark[0]][shark[1]] = 0
    queue = [[shark[0], shark[1]]]

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] <= size and temp[nx][ny] == -1:
                    temp[nx][ny] = temp[x][y] + 1
                    queue.append([nx, ny])

    prey = []
    for i in range(N):
        for j in range(N):
            if 0 < temp[i][j] and 0 < arr[i][j] < size:
                prey.append([i, j, temp[i][j]])
    if len(prey) == 0:
        break
    elif len(prey) == 1:
        answer += prey[0][2]
        arr[shark[0]][shark[1]] = 0
        shark = [prey[0][0], prey[0][1]]
        arr[prey[0][0]][prey[0][1]] = 9
        number += 1
        continue

    prey.sort(key=lambda l: (l[-1], l[0], l[1]))
    answer += prey[0][2]
    arr[shark[0]][shark[1]] = 0
    shark = [prey[0][0], prey[0][1]]
    arr[prey[0][0]][prey[0][1]] = 9
    number += 1

print(answer)
