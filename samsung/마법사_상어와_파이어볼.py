dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fireball = []

for _ in range(M):
    ri, ci, mi, si, di = map(int, input().split())
    fireball.append([ri - 1, ci - 1, mi, si, di])


for _ in range(K):
    current = [[[] for _ in range(N)] for _ in range(N)]
    length = len(fireball)

    for _ in range(length):
        r, c, m, s, d = fireball.pop(0)
        nr = (r + dx[d] * s) % N
        nc = (c + dy[d] * s) % N
        current[nr][nc].append([m, s, d])

    for i in range(N):
        for j in range(N):
            number = len(current[i][j])
            if number == 1:
                m, s, d = current[i][j][0]
                fireball.append([i, j, m, s, d])
            elif number > 1:
                check = True
                sum_m, sum_s, nd = current[i][j][0]
                for k in range(1, number):
                    m, s, d = current[i][j][k]
                    sum_m += m
                    sum_s += s
                    if nd % 2 != d % 2:
                        check = False
                sum_m //= 5
                if sum_m > 0:
                    sum_s //= number
                    if check:
                        fireball.append([i, j, sum_m, sum_s, 0])
                        fireball.append([i, j, sum_m, sum_s, 2])
                        fireball.append([i, j, sum_m, sum_s, 4])
                        fireball.append([i, j, sum_m, sum_s, 6])
                    else:
                        fireball.append([i, j, sum_m, sum_s, 1])
                        fireball.append([i, j, sum_m, sum_s, 3])
                        fireball.append([i, j, sum_m, sum_s, 5])
                        fireball.append([i, j, sum_m, sum_s, 7])
answer = 0
for r, c, m, s, d in fireball:
    answer += m

print(answer)
