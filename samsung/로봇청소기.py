dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

visited[r][c] = True
answer = 1

while True:
    found = False
    for _ in range(4):
        d = (d + 3) % 4
        nr, nc = r + dx[d], c + dy[d]
        if graph[nr][nc] == 0 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            r, c = nr, nc
            answer += 1
            found = True
            break
    if not found:
        if graph[r - dx[d]][c - dy[d]] == 1:
            break
        r, c = r - dx[d], c - dy[d]

print(answer)
