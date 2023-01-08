N, M, D = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def deepcopy(mutable):
    if type(mutable) != list:
        return mutable
    now = []
    for item in mutable:
        now.append(deepcopy(item))
    return now


def check(temp):
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 1:
                return False
    return True


def move(temp):
    new_data = [[0] * M for _ in range(N)]
    for i in range(1, N):
        for j in range(M):
            new_data[i][j] = temp[i - 1][j]
    return new_data


def solve(archers):
    current = deepcopy(graph)
    result = 0
    while True:
        if check(current):
            break
        enemy = []
        for ay in archers:
            temp = []
            for i in range(N):
                for j in range(M):
                    if abs(N - i) + abs(ay - j) <= D:
                        if current[i][j] == 1:
                            temp.append([i, j, abs(N - i) + abs(ay - j)])
            if not temp:
                continue
            temp.sort(key=lambda l: (l[-1], l[1]))
            enemy.append([temp[0][0], temp[0][1]])
        for ex, ey in enemy:
            if current[ex][ey] == 1:
                result += 1
                current[ex][ey] = 0
        current = move(current)
    return result


def position(start, archers):
    global answer
    if len(archers) == 3:
        answer = max(answer, solve(archers))
        return
    for i in range(start, M):
        archers.append(i)
        position(i + 1, archers)
        archers.pop()


position(0, [])
print(answer)
