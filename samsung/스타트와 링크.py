N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

answer = int(1e9)


def solve(index, team_start):
    global answer
    if len(team_start) == N / 2:
        team_link = []
        for i in range(N):
            if i not in team_start:
                team_link.append(i)
        length = len(team_start)
        start, link = 0, 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                sx, sy = team_start[i], team_start[j]
                lx, ly = team_link[i], team_link[j]
                start += graph[sx][sy] + graph[sy][sx]
                link += graph[lx][ly] + graph[ly][lx]
        answer = min(answer, abs(start - link))
        return
    for i in range(index, N):
        team_start.append(i)
        solve(i + 1, team_start)
        team_start.pop()


solve(0, [])
print(answer)
