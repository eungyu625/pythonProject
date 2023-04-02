N = int(input())
inning = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def solve(lineup):
    global answer
    lineup = list(lineup[:3]) + [0] + list(lineup[3:])
    result, player = 0, 0
    for n in range(N):
        base_1, base_2, base_3 = 0, 0, 0
        out = 0
        while out < 3:
            now = inning[n][lineup[player]]
            player = (player + 1) % 9
            if now == 0:
                out += 1
            elif now == 1:
                result += base_3
                base_1, base_2, base_3 = 1, base_1, base_2
            elif now == 2:
                result += base_2 + base_3
                base_1, base_2, base_3 = 0, 1, base_1
            elif now == 3:
                result += base_1 + base_2 + base_3
                base_1, base_2, base_3 = 0, 0, 1
            else:
                result += 1 + base_1 + base_2 + base_3
                base_1, base_2, base_3 = 0, 0, 0
    answer = max(answer, result)


def permutation(index, temp):
    if index == 8:
        solve(temp)
        return
    for i in range(1, 9):
        if i in temp:
            continue
        temp.append(i)
        permutation(index + 1, temp)
        temp.pop()


permutation(0, [])
print(answer)
