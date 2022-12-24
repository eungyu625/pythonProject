dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
nutrients = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
death = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)


def spring():
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            trees[i][j].sort()
            length = len(trees[i][j])
            for _ in range(length):
                age = trees[i][j].pop(0)
                if nutrients[i][j] < age:
                    death[i][j].append(age)
                else:
                    nutrients[i][j] -= age
                    trees[i][j].append(age + 1)


def summer():
    for i in range(N):
        for j in range(N):
            if not death[i][j]:
                continue
            while death[i][j]:
                age = death[i][j].pop()
                nutrients[i][j] += age // 2


def fall():
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            for age in trees[i][j]:
                if age % 5 != 0:
                    continue
                for k in range(8):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        trees[nx][ny].append(1)


def winter():
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += arr[i][j]


for _ in range(K):
    spring()
    summer()
    fall()
    winter()

alive = 0
for a in range(N):
    for b in range(N):
        alive += len(trees[a][b])

print(alive)
