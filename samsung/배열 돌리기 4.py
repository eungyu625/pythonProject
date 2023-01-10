from itertools import permutations

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rotations = list(permutations([list(map(int, input().split())) for _ in range(K)]))
answer = int(1e9)


def deepcopy(mutable):
    if type(mutable) != list:
        return mutable
    now = []
    for item in mutable:
        now.append(deepcopy(item))
    return now


def solve(current, orders):
    global answer
    for r, c, s in orders:
        r, c = r - 1, c - 1
        sx, sy, ex, ey = r - s, c - s, r + s, c + s
        while sx != ex and sy != ey:
            current[sx][sy + 1], res = current[sx][sy], current[sx][sy + 1]
            nx, ny = sx, sy + 1
            di = 0
            while True:
                nnx, nny = nx + dx[di], ny + dy[di]
                if nnx == sx and nny == sy:
                    current[nnx][nny] = res
                    break
                if nnx < sx or nnx > ex or nny < sy or nny > ey:
                    di = (di + 1) % 4
                    continue
                current[nnx][nny], res = res, current[nnx][nny]
                nx, ny = nnx, nny
            sx, sy, ex, ey = sx + 1, sy + 1, ex - 1, ey - 1

    result = int(1e9)
    for i in range(N):
        score = 0
        for j in range(M):
            score += current[i][j]
        result = min(result, score)
    answer = min(answer, result)


for rotation in rotations:
    solve(deepcopy(arr), rotation)

print(answer)
