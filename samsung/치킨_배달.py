N, M = map(int, input().split())
graph = []
chicken = []
house = []
answer = int(1e9)

for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(len(data)):
        if data[j] == 2:
            chicken.append([i, j])
        if data[j] == 1:
            house.append([i, j])


def solve(current):
    result = 0
    for hx, hy in house:
        res = int(1e9)
        for cx, cy in current:
            res = min(res, abs(cx - hx) + abs(cy - hy))
        result += res
    return result


def choose(cnt, start, current):
    global answer
    if cnt == M:
        answer = min(answer, solve(current))
        return
    for now in range(start, len(chicken)):
        current.append(chicken[now])
        choose(cnt + 1, now + 1, current)
        current.pop()


choose(0, 0, [])
print(answer)
