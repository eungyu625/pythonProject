dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

N, M, K = map(int, input().split())
nutrients = [[5] * N for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)


def tree_sort():
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            trees[i][j].sort()


def spring_summer():
    dead_trees = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            length = len(trees[i][j])
            for k in range(length):
                if trees[i][j][k] <= nutrients[i][j]:
                    nutrients[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, length):
                        dead_trees[i][j] += trees[i][j].pop() // 2
                    break
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += dead_trees[i][j]


def fall():
    for i in range(N):
        for j in range(N):
            if not trees[i][j]:
                continue
            for k in range(len(trees[i][j])):
                if trees[i][j][k] % 5 == 0:
                    for n in range(8):
                        nx, ny = i + dx[n], j + dy[n]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].append(1)


def winter():
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += arr[i][j]


for _ in range(K):
    tree_sort()
    spring_summer()
    fall()
    winter()

answer = 0
for a in range(N):
    for b in range(N):
        answer += len(trees[a][b])

print(answer)
