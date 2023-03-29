N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = int(1e9)


def solve(start, link):
    global answer
    soverall = 0
    loverall = 0
    for i in range(N // 2):
        for j in range(N // 2):
            if i != j:
                soverall += arr[start[i]][start[j]]
                loverall += arr[link[i]][link[j]]
    answer = min(answer, abs(soverall - loverall))


def choose(number, index, start):
    if number == N // 2:
        link = []
        for i in range(N):
            if i not in start:
                link.append(i)
        solve(start, link)
        return
    for i in range(index, N):
        start.append(i)
        choose(number + 1, i + 1, start)
        start.pop()


choose(0, 0, [])

print(answer)
