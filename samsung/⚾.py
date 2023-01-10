from itertools import permutations

N = int(input())
result = [list(map(int, input().split())) for _ in range(N)]
orders = list(permutations([1, 2, 3, 4, 5, 6, 7, 8], 8))
answer = 0

for order in orders:
    lineup = list(order[:3]) + [0] + list(order[3:])
    score, hitter = 0, 0
    for inning in range(N):
        out = 0
        base_1, base_2, base_3 = 0, 0, 0
        while out != 3:
            now = result[inning][lineup[hitter]]
            if now == 0:
                out += 1
            elif now == 1:
                score += base_3
                base_1, base_2, base_3 = 1, base_1, base_2
            elif now == 2:
                score += base_2 + base_3
                base_1, base_2, base_3 = 0, 1, base_1
            elif now == 3:
                score += base_1 + base_2 + base_3
                base_1, base_2, base_3 = 0, 0, 1
            elif now == 4:
                score += 1 + base_1 + base_2 + base_3
                base_1, base_2, base_3 = 0, 0, 0
            hitter = (hitter + 1) % 9
    answer = max(answer, score)

print(answer)
