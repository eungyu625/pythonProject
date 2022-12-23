wheels = [[0] * 8 for _ in range(4)]

for a in range(4):
    data = input()
    for b in range(len(data)):
        wheels[a][b] = int(data[b])

K = int(input())
rotation = []

# 맞닿는 부분 : 1번 2와 2번 6, 2번 2와 3번 6, 3번 2와 4번 6

for _ in range(K):
    rotation.append(list(map(int, input().split())))


def rotate(index, di):
    wheel = wheels[index]
    res = wheel[0]
    if di == 1:
        for w in range(1, 8):
            res, wheel[w] = wheel[w], res
        wheel[0] = res
    else:
        for w in range(7, 0, -1):
            res, wheel[w] = wheel[w], res
        wheel[0] = res


for number, direction in rotation:
    number = number - 1
    one = True if wheels[0][2] != wheels[1][6] else False
    two = True if wheels[1][2] != wheels[2][6] else False
    three = True if wheels[2][2] != wheels[3][6] else False
    rotate(number, direction)

    if number == 0:
        if one:
            direction = -direction
            rotate(number + 1, direction)
            if two:
                direction = -direction
                rotate(number + 2, direction)
                if three:
                    direction = -direction
                    rotate(number + 3, direction)
    if number == 1:
        if one:
            rotate(number - 1, -direction)
        if two:
            direction = -direction
            rotate(number + 1, direction)
            if three:
                direction = -direction
                rotate(number + 2, direction)
    if number == 2:
        if three:
            rotate(number + 1, -direction)
        if two:
            direction = -direction
            rotate(number - 1, direction)
            if one:
                direction = -direction
                rotate(number - 2, direction)
    if number == 3:
        if three:
            direction = -direction
            rotate(number - 1, direction)
            if two:
                direction = -direction
                rotate(number - 2, direction)
                if one:
                    direction = -direction
                    rotate(number - 3, direction)

answer = 0
for i in range(4):
    if wheels[i][0] == 1:
        answer += pow(2, i)

print(answer)
