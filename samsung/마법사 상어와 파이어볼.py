dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireball = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r - 1, c - 1, m, s, d])

for _ in range(K):
    arr = [[[] for _ in range(N)] for _ in range(N)]
    while fireball:
        r, c, m, s, d = fireball.pop()
        nr, nc = (r + dx[d] * s) % N, (c + dy[d] * s) % N
        arr[nr][nc].append([m, s, d])

    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) == 0:
                continue
            if len(arr[i][j]) == 1:
                m, s, d = arr[i][j].pop()
                fireball.append([i, j, m, s, d])
                continue
            mass, speed, even, odd, length = 0, 0, 0, 0, len(arr[i][j])
            for m, s, d in arr[i][j]:
                mass += m
                speed += s
                if d % 2 == 0:
                    even += 1
                else:
                    odd += 1
            mass //= 5
            speed //= length
            if mass == 0:
                continue
            if even == length or odd == length:
                fireball.append([i, j, mass, speed, 0])
                fireball.append([i, j, mass, speed, 2])
                fireball.append([i, j, mass, speed, 4])
                fireball.append([i, j, mass, speed, 6])
            else:
                fireball.append([i, j, mass, speed, 1])
                fireball.append([i, j, mass, speed, 3])
                fireball.append([i, j, mass, speed, 5])
                fireball.append([i, j, mass, speed, 7])

print(sum(f[2] for f in fireball))
