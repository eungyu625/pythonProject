dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, K = int(input()), int(input())
apple = []

for _ in range(K):
    X, Y = map(int, input().split())
    apple.append([X - 1, Y - 1])

L = int(input())
move = []

for _ in range(L):
    X, C = input().split()
    move.append([int(X), C])

snake = [[0, 0]]
direction = 0
answer = 0
m_time, m_di = move.pop(0)

while True:
    answer += 1
    nx, ny = snake[-1][0] + dx[direction], snake[-1][1] + dy[direction]
    if nx >= N or nx < 0 or ny >= N or ny < 0:
        break
    if [nx, ny] in snake:
        break
    if [nx, ny] not in apple:
        snake.append([nx, ny])
        snake.pop(0)
    if [nx, ny] in apple:
        snake.append([nx, ny])
        apple.remove([nx, ny])

    if answer == m_time:
        if m_di == 'L':
            direction = (direction + 3) % 4
        else:
            direction = (direction + 1) % 4

        if move:
            m_time, m_di = move.pop(0)

print(answer)
