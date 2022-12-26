dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
'''
대각선 : 1, 3, 5, 7
'''
answer = 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
move = []
cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

for _ in range(M):
    d, s = map(int, input().split())
    move.append([d - 1, s])


def solve():
    global answer
    for di, si in move:
        # 1단계
        length = len(cloud)
        for _ in range(length):
            cx, cy = cloud.pop(0)
            cloud.append([(cx + dx[di] * si) % N, (cy + dy[di] * si) % N])

        check = [[False] * N for _ in range(N)]
        # 2,3단계
        while cloud:
            cx, cy = cloud.pop(0)
            graph[cx][cy] += 1
            check[cx][cy] = True

        # 4단계
        for i in range(N):
            for j in range(N):
                if not check[i][j]:
                    continue
                res = 0
                for k in range(1, 8, 2):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if graph[nx][ny] > 0:
                            res += 1
                graph[i][j] += res

        # 5단계
        for i in range(N):
            for j in range(N):
                if check[i][j]:
                    continue
                if graph[i][j] >= 2:
                    cloud.append([i, j])
                    graph[i][j] -= 2
    for i in range(N):
        for j in range(N):
            answer += graph[i][j]


solve()
print(answer)
