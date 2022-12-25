N, K = map(int, input().split())
belt = list(map(int, input().split()))
robots = [0] * N
time = 1


def picture():
    print("belt")
    for b in range(N):
        print(belt[b], end=' ')
    print()
    for b in range(2 * N - 1, N - 1, -1):
        print(belt[b], end=' ')
    print()


def first():
    b_res = belt[0]
    for b in range(1, 2 * N):
        b_res, belt[b] = belt[b], b_res
    belt[0] = b_res
    r_res = robots[0]
    for r in range(1, N):
        r_res, robots[r] = robots[r], r_res
    robots[0] = 0
    robots[N - 1] = 0


def second():
    for r in range(N - 2, -1 , -1):
        if robots[r] == 1:
            if robots[r + 1] == 0 and belt[r + 1] > 0:
                robots[r] = 0
                robots[r + 1] = 1
                belt[r + 1] -= 1
    robots[N - 1] = 0


def third():
    if robots[0] == 0 and belt[0] > 0:
        robots[0] = 1
        belt[0] -= 1


while True:
    first()
    second()
    third()
    result = 0
    for i in range(2 * N):
        if belt[i] == 0:
            result += 1
    if result >= K:
        break
    time += 1
print(time)
