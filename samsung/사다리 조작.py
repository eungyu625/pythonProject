N, M, H = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(H + 1)]
answer = int(1e9)

'''
graph[m][n] -> m => m + 1 로 이동
graph[m - 1][n] == 1 -> i = i - 1
'''

for _ in range(M):
    h, n = map(int, input().split())
    graph[h][n] = 1


def check():
    for i in range(1, N + 1):
        res = i
        for j in range(1, H + 1):
            if graph[j][res] == 1:
                res += 1
            elif graph[j][res - 1] == 1:
                res -= 1
        if res != i:
            return False
    return True


def no_ladder():
    global answer
    if check():
        answer = min(answer, 0)


def make_ladder_one():
    global answer
    for i in range(1, H + 1):
        for j in range(1, N):
            if graph[i][j - 1] == 0 and graph[i][j + 1] == 0 and graph[i][j] == 0:
                graph[i][j] = 1
                if check():
                    answer = min(answer, 1)
                    return
                graph[i][j] = 0


def make_ladder_two(cnt):
    global answer
    if cnt == 2:
        if check():
            answer = min(answer, 2)
        return
    for i in range(1, H + 1):
        for j in range(1, N):
            if graph[i][j - 1] == 0 and graph[i][j + 1] == 0 and graph[i][j] == 0:
                graph[i][j] = 1
                make_ladder_two(cnt + 1)
                graph[i][j] = 0


def make_ladder_three(cnt):
    global answer
    if cnt == 3:
        if check():
            answer = min(answer, 3)
        return
    for i in range(1, H + 1):
        for j in range(1, N):
            if graph[i][j - 1] == 0 and graph[i][j + 1] == 0 and graph[i][j] == 0:
                graph[i][j] = 1
                make_ladder_three(cnt + 1)
                graph[i][j] = 0


no_ladder()
if answer != 0:
    make_ladder_one()
    if answer != 1:
        make_ladder_two(0)
        if answer != 2:
            make_ladder_three(0)
            if answer != 3:
                print(-1)
            else:
                print(3)
        else:
            print(2)
    else:
        print(1)
else:
    print(0)
